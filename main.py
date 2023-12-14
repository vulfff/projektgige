import backtrader
import datetime
from andmed_GUI import BacktestApp
from backtester import strateegia
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

# Funktsioon, mis teostab läbi backtraderi kauplemise.
def põhikood(rahasumma,failitee,riskiprotsent,indikaatorid):
    # Funktsioon, mis käivitab backtraderi
    cerebro = backtrader.Cerebro()
    # Kasutaja poolt antud summa määratakse portfelli suuruseks
    cerebro.broker.set_cash(float(rahasumma))
    # Faili andmete lugemine
    andmed=backtrader.feeds.YahooFinanceCSVData(                                        
        dataname=failitee,                                                                                                                                                 
    )                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    # Kasutaja poolt antud riskiprotsent määratakse muutujale.
    cerebro.risk=riskiprotsent
    # Indikaatorid ka
    cerebro.valik=indikaatorid
    # Põhirogrammi lisatakse andmed, mis just sisse loeti
    cerebro.adddata(andmed)
    # Põhiprogrammi lisatakse strateegia backtester.py failist
    cerebro.addstrategy(strateegia)

    print('Portfelli suurus enne kauplemist: %.2f' % cerebro.broker.getvalue())
    # Programm hakkab strateegiat andmete põhjal läbi mängima
    cerebro.run()

    print('Portfelli lõppväärtus: %.2f' % cerebro.broker.getvalue())
    # Joonistatakse backtraderi sisseehitatud graafik
    cerebro.plot()
# Paneb GUI tööle
def main():
    root = tk.Tk()
    app = BacktestApp(root)

    root.mainloop()

    # Kui GUI pandi lihtsalt kinni, siis ei tehta midagi
    try:
        if app.andmed_olemas: # Kui andmed olemas, siis alustab backtrader testimist
            try:
                põhikood(app.rahasumma, app.failitee, app.riskiprotsent, app.indikaatorid)
            except:
                messagebox.showerror("ERROR", "Viga andmefailiga")
                pass
    except AttributeError:
        pass

if __name__ == "__main__":
    main()