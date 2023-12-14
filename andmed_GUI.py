import tkinter as tk
from tkinter import ttk, filedialog, messagebox


class BacktestApp:
    def __init__(self, master):

        self.master = master
        master.title("Backtester")
        master.configure(bg="#C6C6C6")  # Taustavärv
        
        master.maxsize(550, 650)
        master.minsize(550, 650)
        
        logo = tk.PhotoImage(file="logo.png")
        master.iconphoto(True, logo)
        
        # Stiil entry boxide jaoks
        entry_style = ttk.Style()
        entry_style.configure("TEntry", padding=5, relief="flat", background="#C6C6C6", font=("Helvetica", 16))

        # Pealkiri
        pealkiri_silt = tk.Label(master, text="Sisesta siia andmed testimiseks", font=("Helvetica", 20, "bold"), bg="#C6C6C6")
        pealkiri_silt.pack(pady=(10, 40)) 

        # Rahasumma entry box
        self.rahasumma_silt = tk.Label(master, text="Rahasumma, millega kaupled", font=("Helvetica", 12, "bold"), bg="#C6C6C6")
        self.rahasumma_silt.pack()
        kontroll = (master.register(self.kontrolli_kas_on_number), '%P')
        self.rahasumma_sisestus = ttk.Entry(master, style="TEntry", validate="key", validatecommand=kontroll)
        self.rahasumma_sisestus.pack(pady=5)

        # Riski entry box
        self.riskiprotsent_silt = tk.Label(master, text="Riskiprotsent igal tehingul", font=("Helvetica", 12, "bold"), bg="#C6C6C6")
        self.riskiprotsent_silt.pack()
        kontroll = (master.register(self.kontrolli_kas_on_number), '%P')
        self.riskiprotsent_sisestus = ttk.Entry(master, style="TEntry", validate="key", validatecommand=kontroll)
        self.riskiprotsent_sisestus.pack(pady=5)

        # Faili üleslaadimine
        self.faili_silt = tk.Label(master, text="Vali fail", font=("Helvetica", 12, "bold"), bg="#C6C6C6")
        self.faili_silt.pack()
        self.faili_nupp = ttk.Button(master, text="Kliki siia, et valida fail", command=self.lae_fail, style="TButton")
        self.faili_nupp.pack(pady=5)

        # Indikaatorite checkboxid
        self.checkboxide_silt = tk.Label(master, text="Vali indikaatorid", font=("Helvetica", 12, "bold"), bg="#C6C6C6")
        self.checkboxide_silt.pack()

        self.checkboxide_raam = tk.Frame(self.master, bg="#C6C6C6")
        self.checkboxide_raam.pack(padx=20, pady=5)

        self.indikaatorid = {"Moving average":False, "Exponential moving average":False, "MACD":False, "RSI":False, "LarryR":False}
        self.checkboxid = []

        for i, indikaator in enumerate(self.indikaatorid):
            muutuja = tk.IntVar()
            self.checkbox = tk.Checkbutton(self.checkboxide_raam, variable=muutuja, text=indikaator, font=("Helvetica", 10), bg="#C6C6C6", selectcolor="#C6C6C6")
            self.checkbox.grid(row=i, column=1, sticky="w", padx=180)
            self.checkboxid.append(muutuja)

        # Kinnita nupp
        self.kinnita_nupp = ttk.Button(master, text="Kinnita andmed ja alusta", command=self.võta_väärtused, style="Bold.TButton")
        self.kinnita_nupp.pack(pady = (40, 20))

        # Kinnita nupu stiil
        nupu_stiil = ttk.Style()
        nupu_stiil.configure("Bold.TButton", padding=5, relief="flat", background="#C6C6C6", foreground="#000000", font=("Helvetica", 18, "bold"))
        nupu_stiil.map("Bold.TButton", background=[("active", "#C6C6C6")])
        
        # Faili üleslaadimise nupu stiil
        nupu_stiil2 = ttk.Style()
        nupu_stiil2.configure("TButton", padding=5, relief="flat", background="#C6C6C6", foreground="#AFAFAF", font=("Helvetica", 10, "bold"),)
        nupu_stiil2.map("TButton", background=[("active", "#C6C6C6")])
        
        # Defineerin 'rooti', et põhifailis sellele paremini ligi saaks
        self.root=master

        # Iga kord kui midagi entry boxi sisestatakse, siis kontrollib kas input on numerical
    def kontrolli_kas_on_number(self, input):
        if not input:
            return True  # Lubab kustutada

        try:
            float(input)
            if " " in input:
                return False
            return True
        except ValueError:
            return False
    
        # Läheb tööle, kui faili nupp on vajutatud
    def lae_fail(self):
        failitee = filedialog.askopenfilename()
        self.faili_silt.config(text=f"Valitud fail: {failitee}")
        
        # Läheb tööle, kui kinnita nupp on vajutatud
    def võta_väärtused(self):
        self.rahasumma = self.rahasumma_sisestus.get()
        self.riskiprotsent = self.riskiprotsent_sisestus.get()
        self.failitee = self.faili_silt.cget("text").replace("Valitud fail: ", "")
        
        if self.rahasumma == "" or self.riskiprotsent == "" or self.failitee == "Vali fail" or (not any(list(map(bool, [muutuja.get() for muutuja in self.checkboxid])))):
            messagebox.showerror("ERROR", "Kontrolli üle sisestus")
        else:
            self.checkboxid = list(map(bool, [muutuja.get() for muutuja in self.checkboxid]))
            for i, indikaator in enumerate(self.indikaatorid):  # Teeb sõnastiku indikaatoritest ja nende väärtustest
                self.indikaatorid[indikaator] = self.checkboxid[i]
            self.andmed_olemas = True
            print(self.indikaatorid)
            self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = BacktestApp(root)

    root.mainloop()