import backtrader
import datetime
from eurusd_strat import eurusd

cerebro = backtrader.Cerebro()

cerebro.broker.set_cash(100000)

data=backtrader.feeds.YahooFinanceCSVData(
    dataname='EURUSD.csv',                                     # EUR/USD kursi ajaloolistel liikumistel põhinev csv fail
    fromdate=datetime.datetime(2018, 11, 1), 
    todate=datetime.datetime(2022, 11, 1), 
    reverse=False)

cerebro.adddata(data)

cerebro.addstrategy(eurusd)

cerebro.addsizer(backtrader.sizers.FixedSize, stake=1000000) # ostetakse/müüakse miljoni jagu dollareid, kui kontol ainult 100000: antud olukorras reaalne, kuna arvestame võimendusega, mida enamus maaklerid pakuvad

print('Starting portfolio value: %.2f' % cerebro.broker.getvalue())

cerebro.run()

print('Final portfolio value: %.2f' % cerebro.broker.getvalue())

cerebro.plot()
