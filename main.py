from numpy import random
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import time

class Henkilo():
    def __init__(self):
        self.nimi_henkilo = ""
        self.huutaa = "VOI EI!"
        
class Auto():
    def __init__(self):
        self.nimi_auto = ""
        self.kuljettaja = Henkilo()
        self.polttoaine_1km = 0
        self.polttoaine = 50
        self.km_perille = 0
        self.matka = 0
        self.matkamittari = 0
        self.renkaat = []
    def renkaat_auto(self):
        laskuri = 0
        while laskuri < 4:
            rengas_auto = Rengas()
            self.renkaat.append(rengas_auto)
            laskuri += 1
    def liiku(self):
        self.polttoaine -= self.polttoaine_1km
        self.polttoaine = round(self.polttoaine,2)
        self.matkamittari += 1
        self.matka += 1
        tekstikentta_polttoaine.delete(0, tk.END) 
        tekstikentta_polttoaine.insert(0, str(self.polttoaine))
        polttoaine_bar["value"] = self.polttoaine
        tekstikentta_matkamittari.delete(0, tk.END) 
        tekstikentta_matkamittari.insert(0, str(self.matkamittari))
        laskuri = 0
        while laskuri < 4:
            rengas_auto = self.renkaat[laskuri]
            m = random.randint(1000)
            if m == 0:
                rengas_auto.ehja = 0
            tekstikentat_renkaat[laskuri].delete(0, tk.END) 
            tekstikentat_renkaat[laskuri].insert(0, str(rengas_auto.ehja))
            laskuri += 1 
    
class Rengas():
    def __init__(self):
        self.ehja = 1
    
mun_auto = Auto()



class Kartta():
    def __init__(self):
        self.tie = []
        self.auto = mun_auto
    def tie_auto(self):
        laskuri = 0
        while laskuri < 30:
            self.tie.append("_")
            laskuri += 1
    
salo = Kartta()
mun_auto.nimi_auto = "Nota"
mun_auto.polttoaine_1km = 0.06
mun_auto.kuljettaja.nimi_henkilo = "Matti"
mun_auto.renkaat_auto()
mun_auto.km_perille = 0
mun_auto.matka = 0

ikkuna = tk.Tk()
ikkuna.title("Auton liikkuminen")
ikkuna.geometry("600x1000")

polttoaine_frame = tk.LabelFrame(ikkuna, text="Polttoaine", width=100, height=50)
polttoaine_frame.pack(padx=10, pady=5, fill='x')

polttoaine_tankki_label = tk.Label(polttoaine_frame, text="Tankissa on bensaa", fg="green", font=("Arial", 12),width=30)
polttoaine_tankki_label.pack(padx=10, pady=5)

tekstikentta_polttoaine = tk.Entry(polttoaine_frame, width=5)
tekstikentta_polttoaine.pack(padx=10, pady=5)

polttoaine_bar = Progressbar(polttoaine_frame,orient=HORIZONTAL,length=250,mode="determinate",maximum=50)
polttoaine_bar.pack(pady=5)
polttoaine_bar["value"] = mun_auto.polttoaine

def tankata():
    mun_auto.polttoaine = 50
    polttoaine_bar["value"] = mun_auto.polttoaine
    tekstikentta_polttoaine.delete(0, tk.END) 
    tekstikentta_polttoaine.insert(0, str(mun_auto.polttoaine))
    polttoaine_tankki_label.config(text="")
    polttoaine_tankki_label.config(text="Tankissa on bensaa", fg="green")
    rikki_auto_label.config(text="")
    rikki_auto_label.config(text="Auto on valmiina", fg="green")
    kartta_canvas.itemconfig(auto_kuva, fill="blue")
    laskuri = 0
    km_perille = mun_auto.km_perille
    while laskuri < km_perille:            
        mun_auto.liiku()
        paivita_auto_kartalla()
        ikkuna.update_idletasks()
        nopeus = speed_scale.get()
        time.sleep(1 / nopeus)
        mun_auto.km_perille -= 1
        laskuri_rengas = 0
        while laskuri_rengas < 4:
            rengas_auto = mun_auto.renkaat[laskuri_rengas]
            if rengas_auto.ehja == 0:
                rikki_rengas_label.config(text="")
                rikki_rengas_label.config(text="Renkaassa on reikä", fg="red")
                kartta_canvas.itemconfig(auto_kuva, fill="red")
                print(mun_auto.kuljettaja.huutaa)
                laskuri_rengas = 4
            laskuri_rengas += 1
        if mun_auto.polttoaine <= 1:
            polttoaine_tankki_label.config(text="")
            polttoaine_tankki_label.config(text="Tankissa ei ole polttoainetta", fg="red")
            kartta_canvas.itemconfig(auto_kuva, fill="red")
            break
        if rengas_auto.ehja == 0:
            break
        laskuri += 1
    if mun_auto.km_perille == 0:
        mun_auto.matka = 0

nappula_polttoaine = tk.Button(polttoaine_frame, text="Tankata",command=tankata) 
nappula_polttoaine.pack(padx=10, pady=5)

matkamittari_frame = tk.LabelFrame(ikkuna, text="Matkamittari", width=100, height=50)
matkamittari_frame.pack(padx=10, pady=5, fill='x')

tekstikentta_matkamittari = tk.Entry(matkamittari_frame, width=5)
tekstikentta_matkamittari.pack(padx=10, pady=5)

def paivitys():
    mun_auto.matkamittari = 0
    tekstikentta_matkamittari.delete(0, tk.END) 
    tekstikentta_matkamittari.insert(0, str(mun_auto.matkamittari))


nappula_matkamittari = tk.Button(matkamittari_frame, text="Päivitys",command=paivitys) 
nappula_matkamittari.pack(padx=10, pady=5)

renkaat_frame = tk.LabelFrame(ikkuna, text="Renkaat", width=100, height=50)
renkaat_frame.pack(padx=10, pady=5, fill='x')

renkaat_labels = ["Rengas 1", "Rengas 2", "Rengas 3","Rengas 4"]
tekstikentat_renkaat = []

for label in renkaat_labels:
    slider_frame = tk.Frame(renkaat_frame)
    slider_frame.pack(fill='x', padx=10, pady=5)
    tk.Label(slider_frame, text=label, width=10).pack(side=tk.LEFT)
    tekstikentta_rengas = tk.Entry(slider_frame, width=5)
    tekstikentta_rengas.place(x=100, y=3)
    tekstikentat_renkaat.append(tekstikentta_rengas)

rikki_rengas_label = tk.Label(renkaat_frame, text="Renkaat kunnossa", fg="green", font=("Arial", 12),width=30)
rikki_rengas_label.place(x=200, y=90)

def vaihda_renkaat():
    laskuri = 0
    while laskuri < 4:
        rengas_auto = mun_auto.renkaat[laskuri]
        rengas_auto.ehja = 1
        tekstikentat_renkaat[laskuri].delete(0, tk.END) 
        tekstikentat_renkaat[laskuri].insert(0, str(rengas_auto.ehja))
        laskuri += 1
    rikki_rengas_label.config(text="")
    rikki_rengas_label.config(text="Renkaat kunnossa", fg="green")
    rikki_auto_label.config(text="")
    rikki_auto_label.config(text="Auto on valmiina", fg="green")
    kartta_canvas.itemconfig(auto_kuva, fill="blue")
    laskuri = 0
    km_perille = mun_auto.km_perille
    while laskuri < km_perille:            
        mun_auto.liiku()
        paivita_auto_kartalla()
        ikkuna.update_idletasks()
        nopeus = speed_scale.get()
        time.sleep(1 / nopeus)
        mun_auto.km_perille -= 1
        laskuri_rengas = 0
        while laskuri_rengas < 4:
            rengas_auto = mun_auto.renkaat[laskuri_rengas]
            if rengas_auto.ehja == 0:
                rikki_rengas_label.config(text="")
                rikki_rengas_label.config(text="Renkaassa on reikä", fg="red")
                kartta_canvas.itemconfig(auto_kuva, fill="red")
                print(mun_auto.kuljettaja.huutaa)
                laskuri_rengas = 4
            laskuri_rengas += 1
        if mun_auto.polttoaine <= 1:
            polttoaine_tankki_label.config(text="")
            polttoaine_tankki_label.config(text="Tankissa ei ole polttoainetta", fg="red")
            kartta_canvas.itemconfig(auto_kuva, fill="red")
            break
        if rengas_auto.ehja == 0:
            break
        laskuri += 1
    if mun_auto.km_perille == 0:
        mun_auto.matka = 0
    
nappula_tarkastus = tk.Button(renkaat_frame, text="Vaihda renkaat",command=vaihda_renkaat) #funktio kytketään nappulan painamiseen
nappula_tarkastus.place(x=300, y=50)

kaupunki_frame = tk.LabelFrame(ikkuna, text="Kaupunki", width=100, height=50)
kaupunki_frame.pack(padx=10, pady=10, fill='x')

v = StringVar(kaupunki_frame,"1")
values = {"Karjaa-Salo (67km)" : "1", 
        "Karjaa-Tammisaari (19km)" : "2", 
        "Karjaa-Helsinki (76km)" : "3", 
        "Karjaa-Lohja (33km)" : "4", 
        "Karjaa-Inkoo (20km)" : "5"}
for (text, value) in values.items(): 
    Radiobutton(kaupunki_frame, text = text, variable = v, value = value).pack(side = TOP, ipady = 5)

rikki_auto_label = tk.Label(kaupunki_frame, text="Auto on valmiina", fg="green", font=("Arial", 12))
rikki_auto_label.pack(pady=10)

def start_ajo():
    global auto_kuva
    if v.get() == "1":
        km = 67
    if v.get() == "2":
        km = 19
    if v.get() == "3":
        km = 76
    if v.get() == "4":
        km = 33
    if v.get() == "5":
        km = 20
    laskuri = 0
    for r in mun_auto.renkaat:
        if r.ehja == 0:
            rikki_auto_label.config(text="")
            rikki_auto_label.config(text="Rikkoutunut pyörä pitää vaihtaa", fg="red")
            laskuri = km
    if mun_auto.polttoaine <= 1:
        rikki_auto_label.config(text="")
        rikki_auto_label.config(text="Auto pitää tankata", fg="red")
        laskuri = km
    if laskuri != km:
        mun_auto.km_perille = km
        kartta_canvas.delete("all")
        karta()
        auto_kuva = kartta_canvas.create_rectangle(10, 30, 14, 45, fill="blue")
    while laskuri < km:            
        mun_auto.liiku()
        paivita_auto_kartalla()
        ikkuna.update_idletasks()
        nopeus = speed_scale.get()
        time.sleep(1 / nopeus)
        mun_auto.km_perille -= 1
        laskuri_rengas = 0
        while laskuri_rengas < 4:
            rengas_auto = mun_auto.renkaat[laskuri_rengas]
            if rengas_auto.ehja == 0:
                rikki_rengas_label.config(text="")
                rikki_rengas_label.config(text="Renkaassa on reikä", fg="red")
                kartta_canvas.itemconfig(auto_kuva, fill="red")
                print(mun_auto.kuljettaja.huutaa)
                laskuri_rengas = 4
            laskuri_rengas += 1
        if mun_auto.polttoaine <= 1:
            polttoaine_tankki_label.config(text="")
            polttoaine_tankki_label.config(text="Tankissa ei ole polttoainetta", fg="red")
            kartta_canvas.itemconfig(auto_kuva, fill="red")
            break
        if rengas_auto.ehja == 0:
            break
        laskuri += 1
    if mun_auto.matka == km:
        mun_auto.matka = 0

matka_frame = tk.LabelFrame(ikkuna, text="Matka", width=100, height=50)
matka_frame.pack(padx=10, pady=10, fill='x')

kartta_canvas = tk.Canvas(matka_frame, width=500, height=80, bg="white")
kartta_canvas.pack(pady=10)

def karta():
    pisteet = []
    laskuri = 0
    while laskuri < mun_auto.km_perille:
        x = 10 + laskuri * 6
        y = 40
        piste = kartta_canvas.create_oval(x, y, x+3, y+3, fill="gray")
        pisteet.append(piste)
        laskuri += 1
auto_kuva = kartta_canvas.create_rectangle(10, 30, 14, 45, fill="blue")

def paivita_auto_kartalla():
    x = 10 + mun_auto.matka * 6
    y = 40
    kartta_canvas.coords(auto_kuva, x, y-10, x+15, y+5)

speed_scale = tk.Scale(matka_frame, from_=1, to=10, orient=HORIZONTAL,label="Nopeus")
speed_scale.set(5)
speed_scale.pack(pady=10)

nappula_start = tk.Button(ikkuna, text="Start",command=start_ajo) #funktio kytketään nappulan painamiseen
nappula_start.pack(padx=10, pady=10)

ikkuna.mainloop()
