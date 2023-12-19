# projektGIGE

## Algeline kauplemissimulaator
Projekt Gige puhul on tegemist algelise kauplemissimulaatoriga.  
Tööpõhimõte on programmil lihtne: otsid ![Yahoost](https://finance.yahoo.com/) meeldiva finantsvara, valid lahtri 'Historical data', määrad vabalt valitud ajaperioodi ja sisestad Yahoo poolt antud .csv faili programmi.
Programm töötab üldjuhul ainult andmetel, mis Yahoo portaalist saadaval, kuna enamuste teiste portaalide failides on hindade ja kuupäevade järjestus tavaliselt erinev. Programm on suuteline kauplema põhinevalt viiel populaarsel indikaatoril, valiku teeb kasutaja (indikaatorid on funktsioonid, mis on tuletatud vara hinna muutusest ning mis proovivad teada anda kauplejale soodsatest hetkedest tehingute tegemiseks). Programmi käivitamisel jooksevad teavitused kõikidest tehingutest kui ka konto lõppsuurusest terminali.


Antud projektis on suures osas kasutatud ![backtraderi](https://github.com/mementum/backtrader) teeki, mis on Pythonil põhinev algoritmkauplemist võimaldav teek.

### Programmi sisu
* Kasutajasõbralik GUI
* Tulemust illustreeriv graafik
* 5 erinevat indikaatorit:
  * ![SMA](https://www.investopedia.com/terms/s/sma.asp)
  * ![EMA](https://www.investopedia.com/terms/e/ema.asp)
  * ![MACD](https://www.investopedia.com/terms/m/macd.asp)
  * ![RSI](https://www.investopedia.com/terms/r/rsi.asp)
  * ![LarryR](https://www.investopedia.com/terms/w/williamsr.asp)
