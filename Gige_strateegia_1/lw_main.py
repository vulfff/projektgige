import backtrader                                                                   # toob programmi backtrader 'frameworki'
import backtrader.feeds as btfeeds
import os
import sys
import datetime
from lw_strateegia import LW_Strategy                                                # impordib strateegia teisest failist
import matplotlib as plt

cerebro = backtrader.Cerebro()                                                      # toob simulatsioniliidese programmi

cerebro.broker.set_cash(100000)                                                     # määrab konto rahalise suuruse  kuigi futuuridega kaubeldes ei mängi rolli(pigem vaja forexis/stockides jms)

data=backtrader.feeds.GenericCSVData(                                               # muutujale antakse turuandmed funktsiooni abil
    dataname='eminiSP500.csv',                                                         # csv fail kust võetakse andmed
    fromdate=datetime.datetime(2021, 11, 1),                                        # määrad kuupäeva, kus strateegiat alustad/andmeid võtma hakkad
    todate=datetime.datetime(2023, 10, 1),                                          # määrad kuupäeva, kus strateegia lõppeb/andmed saavad otsa
    dtformat=('%Y-%m-%d'),                                                          # failis kehtestatud datetime format
    timeframe=backtrader.TimeFrame.Days,                                            # hinnad võetakse päeva kaupa
    reverse=False)

cerebro.adddata(data)                                                               # turuandmed sisestatakse kauplemisprogrammile

cerebro.addstrategy(LW_Strategy)                                                    # lisab programmile varem lisatud strateegia

cerebro.addsizer(backtrader.sizers.FixedSize, stake=1)                              # määrab positsioonisuuruse

print('Starting portfolio value: %.2f' % cerebro.broker.getvalue())                 # tagastab kontojäägi, saab ka lõpus tagastada, kuid futuuridega kaubeldes see meid ei huvita 

cerebro.run()                                                                       # käivitab simulatsiooni


cerebro.plot()                                                                      # väljastab lihtsa graafiku