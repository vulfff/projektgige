import backtrader
from andmed_GUI import BacktestApp
# Moving average
# Exponential moving  average
# MACD
# RSI
# LarryR

class strateegia(backtrader.Strategy):
    params = (
        ('macd1',12),
        ('macd2',26),
        ('macdsig',9),
    )
    
    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        self.valik=[True,True,True,True,True]
        self.kordaja=float(self.cerebro.risk)/100
        self.dataclose = self.datas[0].close
        self.order=None
        self.williams = backtrader.indicators.WilliamsR(self.data, period=14)
        self.sma = backtrader.indicators.SMA(self.dataclose, period=9)
        self.macd = backtrader.indicators.MACD(self.dataclose,
                                             period_me1=self.params.macd1,
                                             period_me2=self.params.macd2,
                                             period_signal=self.params.macdsig)
        self.ema = backtrader.indicators.ExponentialMovingAverage(self.dataclose, period=9)
        self.rsi=backtrader.indicators.RelativeStrengthIndex(self.dataclose, period=14)

    def ost(self):
        ostu_tingimused = [
        (self.valik[0] and self.williams <= -80),
        (self.valik[1] and self.dataclose[0] < self.sma),
        (self.valik[2] and self.macd > 0),
        (self.valik[3] and self.dataclose[0] < self.ema),
        (self.valik[4] and self.rsi <= 30),
    ]
        return any(tingimus for tingimus in ostu_tingimused)

    def müük(self):
        müügi_tingimused = [
        (self.valik[0] and self.williams >= -20),
        (self.valik[1] and self.dataclose[0] > self.sma),
        (self.valik[2] and self.macd < 0),
        (self.valik[3] and self.dataclose[0] > self.ema),
        (self.valik[4] and self.rsi >= 70),
    ]
        return any(tingimus for tingimus in müügi_tingimused)

    
    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log('OST SOORITATUD {}'.format(order.executed.price))
            elif order.issell():
                self.log('MÜÜK SOORITATUD {}'.format(order.executed.price))
            
            self.bar_executed=len(self)

        self.order=None

    def next(self):
        cash=self.cerebro.broker.getcash()

        if self.order:
            return
        if not self.position:
            if self.ost():
                self.stake=cash/self.dataclose[0]
                self.order=self.buy(size=self.stake)                              
                self.type='buy'
                self.orderday=self.dataclose[0]
                self.log('OSTUTEHING SOORITATUD {}'.format(self.dataclose[0]))
            elif self.müük():
                self.stake=cash/self.dataclose[0]
                self.order=self.sell(size=self.stake)               
                self.type='sell'
                self.orderday=self.dataclose[0]
                self.log('MÜÜGITEHING SOORITATUD {}'.format(self.dataclose[0]))
        else:
            if self.type == 'buy' and self.müük() or (self.dataclose[0]-self.orderday)*self.stake >= cash*self.kordaja:     
                self.order=self.close(size=self.stake)
                self.log('POSITSIOON SULETUD {}'.format(self.dataclose[0]))
            elif self.type == 'sell' and self.ost() or (self.orderday-self.dataclose[0])*self.stake >= cash*self.kordaja:      
                self.order=self.close(size=self.stake)
                self.log('POSITSIOON SULETUD {}'.format(self.dataclose[0]))