import backtrader


class eurusd(backtrader.Strategy):
    params = (                                  # parameeter indikaatori jaoks
        ('period',14),
    )
    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        self.dataclose = self.datas[0].close
        self.order=None
        self.williams = backtrader.indicators.WilliamsR(self.data, period=self.params.period) # toon sisse WilliamsR indikaatori - see proovib anda aimu, kas instrument on ülemüüdud/üleostetud

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log('BUY EXECUTED {}'.format(order.executed.price))
            elif order.issell():
                self.log('SELL EXECUTED {}'.format(order.executed.price))
            
            self.bar_executed=len(self)

        self.order=None

    def next(self):
        williams_value=self.williams[0]                            # toob sisse muutuja, mille väljastab WilliamsR indikaator, vahemik on tal 0 kuni -100
        self.log('Close, %.2f' % self.dataclose[0])
        if self.order:
            return
        if not self.position:
            if williams_value <= -80:                              # mida madalam on arv vahemikus, seda rohkem on instrument ülemüüdud, -80 ja madalam annab algoritmile ostmissignaali
                self.order=self.buy()
                self.type='buy'

            elif williams_value >= -20:                            # mida suurem on arv vahemikus, seda rohkem on instrument üleostetud, -20 ja kõrgem annab algoritmile ostmissignaali
                self.order=self.sell()
                self.type='sell'
        else:
            if self.type=='sell' and williams_value >= -20:        # algoritm sulgeb müügipositsiooni, kui instrument on indikaatori arvates ülemüüdud
                self.log('Close created {}'.format(self.dataclose[0]))
                self.order=self.close()
            elif self.type=='buy' and williams_value <= -80:       # algoritm sulgeb ostupositsiooni, kui instrument on indikaatori arvates üleostetud
                self.log('Close created {}'.format(self.dataclose[0]))
                self.order=self.close()