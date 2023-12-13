import backtrader
import datetime
from andmed_GUI import BacktestApp
from backtester import strateegia
import matplotlib.pyplot as plt
import tkinter as tk

def põhikood(rahasumma,failitee,riskiprotsent):

    cerebro = backtrader.Cerebro()

    cerebro.broker.set_cash(float(rahasumma))

    data=backtrader.feeds.YahooFinanceCSVData(                                        
        dataname=failitee,                                                                                                                                                 
    )                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    

    cerebro.risk=riskiprotsent

    cerebro.adddata(data)

    cerebro.addstrategy(strateegia)

    print('Portfelli suurus enne kauplemist: %.2f' % cerebro.broker.getvalue())

    cerebro.run()

    print('Portfelli lõppväärtus: %.2f' % cerebro.broker.getvalue())

    cerebro.plot()

def main():
    root = tk.Tk()
    app = BacktestApp(root)

    root.mainloop()

    # Kui GUI pandi lihtsalt kinni, siis ei tehta midagi
    try:
        if app.andmed_olemas:
            põhikood(app.rahasumma, app.failitee, app.riskiprotsent)
    except AttributeError:
        pass

if __name__ == "__main__":
    main()