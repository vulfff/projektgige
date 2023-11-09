import backtrader
import datetime
from eurusd_strat import eurusd
from oilstrat import oilstrat

cerebro = backtrader.Cerebro()

cerebro.broker.set_cash(100000)

data=backtrader.feeds.YahooFinanceCSVData(
    dataname='eurodollar.csv',                                     # EUR/USD kursi ajaloolistel liikumistel põhinev csv fail
    fromdate=datetime.datetime(2018, 11, 1), 
    todate=datetime.datetime(2023, 11, 1), 
    reverse=False)

cerebro.adddata(data)

cerebro.addstrategy(eurusd)

print('Starting portfolio value: %.2f' % cerebro.broker.getvalue())

cerebro.run()

print('Final portfolio value: %.2f' % cerebro.broker.getvalue())

cerebro.plot()
