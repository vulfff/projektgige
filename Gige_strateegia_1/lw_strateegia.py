import backtrader
import datetime


class LW_Strategy(backtrader.Strategy):                                                                     # strateegia, mida põhiprogramm kasutama hakkab

    def log(self, txt, dt=None):                                                                            # funktsioon, mis peab aja + tehingute järge
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):                                                                                     # strateegiaprogrammi initsialiseerimisfunktsioon, siin saab sisestada strateegiasse indikaatoreid
        self.dataclose = self.datas[0].close
        self.order=None
        self.pnl=0

    def notify_order(self, order):                                                                          # funktsioon mis annab teada, kui algoritm ostab/müüb midagi
        if order.status in [order.Submitted, order.Accepted]:
            return
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log('BUY EXECUTED {}'.format(order.executed.price))
            elif order.issell():
                self.log('SELL EXECUTED {}'.format(order.executed.price))
            
            self.bar_executed=len(self)

        self.order=None

    def next(self):                                                                                         # põhifunktsioon, mis aktiveerub igal sammul, kui analüüsitakse hindasid
        self.log('Close, %.2f' % self.dataclose[0]) 
        print(self.pnl)
        if self.order:
            return
        if not self.position:
            if self.dataclose[0] < self.dataclose[-2] and self.dataclose[-120] < self.dataclose[0]:         # kontrollib kas vaadeldava päeva hind on madalam kui hind 2 päeva tagasi, kuid suurem hinnast 4 kuud tagasi
                    self.entry_price=self.dataclose[0]                                                      # salvestan ostmishinna
                    self.log('BUY CREATE, %.2f' % self.dataclose[0])                                        # väljastan kirja ostutehingust
                    self.order=self.buy()                                                                   # ostutehingu funktsioon   
        else:
            if ((self.entry_price)-(self.dataclose[0]))*50 >= 10000 or ((self.entry_price)-(self.dataclose[0]))*50 <= -4000:    # lahkun tehingust kui kasum on suurem kui 10000 või kahjum suurem kui 4000
                self.log('CLOSE CREATED {}'.format(self.dataclose[0]))                                                          # väljastan kirja positsiooni sulgemistehingust
                self.pnl=self.pnl+((self.entry_price)-(self.dataclose[0]))*50                                                   # hoian järge kasumil/kahjumil
                self.order=self.close()                                                                                         # tehingu sulgemisfunktioon
            