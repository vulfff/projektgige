import backtrader
from andmed_GUI import BacktestApp

class strateegia(backtrader.Strategy):  # Klass, mille põhifailis välja kutsume
    # MACD indikaatori parameetrid
    params = (         
        ('macd1',12),
        ('macd2',26),
        ('macdsig',9),
    )
    # Funktsioon, mis tagastab väljakutsumisel terminali andmetefailist parajasti töödeldava kuupäeva.
    def log(self, txt, dt=None):    
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        self.tehingud=0
        self.valik=self.cerebro.valik   # Toome sisse GUI poolt tehtud kasutaja valikud
        self.kordaja=float(self.cerebro.risk)/100   # Samuti kasutaja sisestatud riskiprotsendi
        self.dataclose = self.datas[0].close    # Defineerime andmestiku järjendi ümber lihtsamini kirjutatavasse vormi.
        self.order=None     # Anname programmi initsialiseerimisel teada, et positsioone pole veel sisestatud.ss

        # Indikaatorite sisse toomine, nende poolt tekkinud väärtuste omistamine.
        if self.valik['LarryR']==True:
            self.williams = backtrader.indicators.WilliamsR(self.data, period=14)
        if self.valik['MACD']==True:
            self.macd = backtrader.indicators.MACD(self.dataclose,
                                                    period_me1=self.params.macd1,
                                                    period_me2=self.params.macd2,
                                                    period_signal=self.params.macdsig,
                                                    )
        if self.valik['Exponential moving average']==True:
            self.ema = backtrader.indicators.ExponentialMovingAverage(self.dataclose, period=9)
        if self.valik['RSI']==True:
            self.rsi=backtrader.indicators.RelativeStrengthIndex(self.dataclose, period=14)
        if self.valik['Moving average']==True:
            self.sma = backtrader.indicators.SMA(self.dataclose, period=9)


    # Funktsioon, mis kontrollib, kas indikaatorite väärtused vihjavad ostmisele.    
    def ost(self):
        ostu_tingimused = [
        (self.valik['LarryR'] and self.williams <= -95),
        (self.valik['Moving average'] and self.dataclose[0] < self.sma and self.dataclose[-1] < self.sma),
        (self.valik['MACD'] and self.macd.macd[0]>self.macd.signal[0] and self.macd.macd[-1]<=self.macd.signal[-1]),
        (self.valik['Exponential moving average'] and self.dataclose[0] < self.ema and  self.dataclose[-1] < self.ema),
        (self.valik['RSI'] and self.rsi <= 15),
    ]
        return any(tingimus for tingimus in ostu_tingimused)

    # Funktsioon, mis kontrollib, kas indikaatorite väärtused vihjavad müümisele.
    def müük(self):
        müügi_tingimused = [
        (self.valik['LarryR'] and self.williams >= -5),
        (self.valik['Moving average'] and self.dataclose[0] > self.sma and self.dataclose[-1] > self.sma),
        (self.valik['MACD'] and self.macd.macd[0]>self.macd.signal[0] and self.macd.macd[-1]<=self.macd.signal[-1]),
        (self.valik['Exponential moving average'] and self.dataclose[0] > self.ema and self.dataclose[-1] > self.ema),
        (self.valik['RSI'] and self.rsi >= 85),
    ]
        return any(tingimus for tingimus in müügi_tingimused)

    # Funktsioon, mis annab terminali kaudu tehingust teada.
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

    # Põhifunktsioon, mis töötleb andmefaili igat rida ja sooritab vastavalt soodsa indikaatori väärtuse korral tehinguid.
    def next(self):
        cash=self.cerebro.broker.getcash()
        # Kui order on olemas, siis ei minda otsima uut positsiooni. Vajalik programmi tööks, kuid praktiline ainult reaalajas kauplemisel.
        if self.order:
            return
        if not self.position:
            # Programm ostab või müüb, kui funktsioonis olevad tingimused on täidetud.
            if self.ost():
                self.stake=cash/self.dataclose[0]
                self.order=self.buy(size=self.stake)                              
                self.type='ost'
                self.orderday=self.dataclose[0]
                self.tehingud+=1
            elif self.müük():
                self.stake=cash/self.dataclose[0]
                self.order=self.sell(size=self.stake)               
                self.type='müük'
                self.orderday=self.dataclose[0]
                self.tehingud+=1
        else:
            # Programm sulgeb positsioonid, kui tingimused on rahuldatud. Ostu positsioon sulgub soodsa müügitingimuse korral ja vastupidi.
            if self.type == 'ost' and self.müük() or (self.dataclose[0]-self.orderday)*self.stake >= cash*self.kordaja:     
                self.order=self.close(size=self.stake)
                self.log('POSITSIOON SULETUD HINNAGA {}'.format(self.dataclose[0]))
                print(f'Tehinguid {self.tehingud}')
            elif self.type == 'müük' and self.ost() or (self.orderday-self.dataclose[0])*self.stake >= cash*self.kordaja:      
                self.order=self.close(size=self.stake)
                self.log('POSITSIOON SULETUD HINNAGA {}'.format(self.dataclose[0]))
                print(f'Tehinguid {self.tehingud}')