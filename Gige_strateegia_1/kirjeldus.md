### 1. kauplemismudel
Kõige esimene kauplemismudel põhineb maailma ühe edukaima futuuridekaupleja Larry Williamsi poolt antud mudelil.  
Mudeli olemus väga lihtne, algoritm tuvastab trendi ning ostab futuuri, kui hind parajasti lühiajalises langemises on.  
Algoritm ootab kuni päeva sulgemishind on madalam kui sulgemishind 2 päeva tagasi, kuid suurem kui hind 120 päeva tagasi.  
Sellised parameetrid iseloomustavad pikaajalist hinna tõusmist, kuid lühiajalist langust.  
Andmed võetakse programmi lw_main.py failist eminiSP500.csv  
eminiSP500.csv, nagu nimi ütleb, sisaldab E-Mini S&P 500 futuuride lepingute hindasid päeva kaupa 2021. aasta novembrist 2023. aasta novembrini.
Põhiprogramm lw_main.py loeb andmed sisse ning seejärel aktiveerib faili lw_strateegia.py, mis sisaldab kauplemisalgoritmi parameetreid.
Kuna tegemist on futuuridega, siis on kasumite/kahjumite arvutamine teistsugune võrreldes teiste varaklassidega.  
Antud juhul on iga 0.25 osa hinna liikumist võrdne 12.5 dollarilise kasumi/kahjumi liikumisega.  
