
# -*- coding: cp1254 -*-
from Tkinter import *

import random
from PIL import ImageTk

pencere = Tk()
gen = pencere.winfo_screenwidth()
yuk = pencere.winfo_screenheight()
pencere.geometry("%sx%s+0+0"%(gen, yuk-50))
pencere.tk_setPalette("green")

def yaz():
        dugme.destroy()

        yazi = Label(pencere, text = u"...Tebrikler Kazandınız...", font = "courel 60 bold", fg = "black")
        yazi.pack(fill = BOTH, expand = YES)

        cerceve = Frame(pencere)
        cerceve.pack(fill = X, pady = 5)

        bilgi = Label(cerceve, text = u"Çıkmak için ekrana tıklatınız.", fg = "black", font = "20")
        bilgi.pack(side = TOP)

        def kapat(event = None):
                pencere.quit()

        pencere.bind("<Button-1>", kapat)

def yakala(event=None):
        k = random.randint(0,gen-150)
        v = random.randint(0,yuk-150)
        
        dugme.place(x=k, y=v)

simge = ImageTk.PhotoImage(file="sinek.jpg")
dugme = Button(image=simge, command=yaz, relief="flat")
dugme.place(x=1, y=0)

dugme.bind("<Enter>", yakala)

mainloop()
