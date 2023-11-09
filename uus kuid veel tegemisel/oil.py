import backtrader
import datetime
from oilstrat import oilstrat
import matplotlib

cerebro = backtrader.Cerebro()

cerebro.broker.set_cash(100000)

data=backtrader.feeds.GenericCSVData(                                               # muutujale antakse turuandmed funktsiooni abil
    dataname='oil2.csv',                                                         # csv fail kust võetakse andmed
    fromdate=datetime.datetime(2006, 11, 1),                                        # määrad kuupäeva, kus strateegiat alustad/andmeid võtma hakkad
    todate=datetime.datetime(2022, 11, 1),                                          # määrad kuupäeva, kus strateegia lõppeb/andmed saavad otsa
    dtformat=('%Y-%m-%d'),                                                       # failis kehtestatud datetime format
    timeframe=backtrader.TimeFrame.Days,
    datetime=0,
    close=1,
    open=2,
    high=3,
    low=4,
    volume=-1,
    openinterest=-1,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              # hinnad võetakse päeva kaupa
    reverse=False)

cerebro.adddata(data)

cerebro.addstrategy(oilstrat)

print('Starting portfolio value: %.2f' % cerebro.broker.getvalue())

cerebro.run()

print('Final portfolio value: %.2f' % cerebro.broker.getvalue())

cerebro.plot(volume=False)