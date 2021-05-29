# -*- coding: cp1254 -*-
"""Furkan Yakın-----22.02.18"""
from tkinter import*
import os
import re
#from tkMessageBox import*
from tkinter import messagebox


class Pencere(object):

    def __init__(self):
        self.pencere_araclari()


    def pencere_araclari(self):

        self.kaydirma = Scrollbar(pencere)
        self.kaydirma.place(relx = 0.90, rely = 0.0, relheight = 0.96)

        self.metin = Text(pencere, yscrollcommand = self.kaydirma.set)
        self.metin.place(relx = 0.0, rely = 0.0, relwidth = 0.9, relheight = 0.96)
        self.metin.focus_set()

        self.kaydirma.config(command = self.metin.yview)

        self.ac_btn = Button(pencere, text = u"Aç", command = toplevel)
        self.ac_btn.place(relx = 0.93, rely = 0.05)
        


        self.kaydet_btn = Button(pencere, text = "Kaydet", command = toplevel2)
        self.kaydet_btn.place(relx = 0.93, rely = 0.13)
        


        self.cikis = Button(pencere, text = u"Çıkış", command = pencere.destroy)
        self.cikis.place(relx = 0.93, rely = 0.21)
        

        self.etiket = Label(pencere, text = u"Dosya Seçiniz")
        self.etiket.place(relx = 0.0, rely = 0.96)

        
        
        pencere.bind("<F1>", toplevel)
        pencere.bind("<F2>", toplevel2)
        
        


class toplevel(Pencere):
    def __init__(self, event = None):
        self.pen2_araclari()
        self.txt_dosyalari = []
        self.dizinler()
        self.listele()
        #self.isaretli()


    def pen2_araclari(self):        
        self.pen2 = Toplevel(pencere)
        self.pen2.title(u"Aç")
        self.pen2.geometry("400x300+500+30")
        self.pen2.resizable(width = False, height = False)

        self.kaydirma = Scrollbar(self.pen2)
        self.kaydirma.place(relx = 0.95, rely = 0.03, relheight = 0.8)

        self.liste = Listbox(self.pen2, yscrollcommand = self.kaydirma.set)
        self.liste.place(relx = 0.02, rely = 0.03, relwidth = 0.93, relheight = 0.8)
        self.liste.focus_set()
        
        self.kaydirma.config(command = self.liste.yview)

        self.sec = Button(self.pen2, text = u"Seç", command = self.secileni_ac)
        self.sec.place(relx = 0.02, rely = 0.87, relwidth = 0.95, relheight = 0.08)

        self.pen2.bind("<Return>", self.secileni_ac)
        
        """
        self.ad = Label(self.pen2, text = u"Dosya Adı:", font = "8")
        self.ad.place(relx = 0.02, rely = 0.87)

        self.adi = Entry(self.pen2)
        self.adi.place(relx = 0.1, rely = 0.87, relwidth = 0.7, relheight = 0.08)
        """
        



    def dizinler(self):
        dosyalar = os.listdir(os.getcwd())
        for i in dosyalar:
            a = ("\.txt$")
            b = re.compile(a)
            c = re.search(b, i)
            if c:
                self.txt_dosyalari.insert(0, i)

    def listele(self):
        if not len(self.txt_dosyalari) == 0:
            for i in self.txt_dosyalari:
                self.liste.insert(END, i)

        """
    def isaretli(self):
        a = self.liste.get(ACTIVE)
        self.adi.delete(0,END)
        self.adi.insert(END,a)
        """       

    def secileni_ac(self, event = None):
        a = self.liste.get(ACTIVE)
        b = open(a, "r")
        c = b.read()
        d = unicode(c, "cp1254")
        p.metin.delete(0.0,END)        
        p.metin.insert(END,d)
        b.close()
        p.etiket["text"] = u"%s Açıldı"%(a)
        self.pen2.destroy()



class toplevel2(Pencere):
    def __init__(self, event = None):
        self.pen3_araclari()

    def pen3_araclari(self):
        self.pen3 = Toplevel(pencere)
        self.pen3.geometry("200x75+700+150")
        self.pen3.resizable(width = False, height = False)

        self.yaz = Label(self.pen3, text = u"Dosya Adını Giriniz")
        self.yaz.pack()

        self.isim = Entry(self.pen3)
        self.isim.pack()
        self.isim.focus_set()

        self.tmm = Button(self.pen3, text = "Tamam", command = self.varmi)
        self.tmm.pack()

        self.pen3.bind("<Return>", self.varmi)
        

    def varmi(self, event = None):
        a = self.isim.get()
        yol = r"C:\Users\furkan\Desktop\%s.txt"%(a)
        dosyalar = os.listdir(os.getcwd())

        if a+".txt" in dosyalar:
            uyari = showwarning(u"Uyarı!", u"Girdiğiniz isimde bir dosya zaten mevcut. Devam etmek istiyormusunuz?",
                                detail = u"Eğer devam ederseniz değişiklikler eski dosyanın üzerine yazılacaktır.",
                                type = YESNO,
                                default = NO)
            if uyari == "yes":
                self.kaydet()

            else:
                toplevel2()

        else:
            self.kaydet()

        
        
    def kaydet(self):
        a = self.isim.get()
        yol = r"C:\Users\furkan\Desktop\%s.txt"%(a)
        b = p.metin.get(1.0, END)
        c = unicode.encode(b, "cp1254")
        dosya = open(yol, "w")
        dosya.write(c)
        dosya.close()
        p.etiket["text"] = u"%s.txt Dosyası Kaydedildi"%(a)
        self.pen3.destroy()
            



        




pencere = Tk()
pencere.geometry("700x500+300+100")
pencere.title("Metin Editörü v1")


p = Pencere()



pencere.mainloop()
