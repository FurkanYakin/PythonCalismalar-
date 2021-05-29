# -*- coding: cp1254 -*-
from Tkinter import*
import smtplib


class Pencere():
    def __init__(self):
        self.giris_pen()

    def giris_pen(self):
        p = pencere
        pencere.resizable(width = False, height = False)
        p.title(u"...Giri� Ekran�...")
        p.bind("<Return>", self.giris)

        self.bilgi = Label(p, text=u"L�tfen kullan�c� bilgilerini giriniz.")
        self.bilgi.place(x=130, y=60)
        
        k_etiketi = Label(p, text = "Gmail Adresiniz :")
        k_etiketi.place(x=120, y=100)

        sifre_etiketi = Label(p, text = u"�ifreniz :")
        sifre_etiketi.place(x=120, y=130)

        self.k_adresi = Entry(p, width=25)
        self.k_adresi.place(x=220, y=100)
        self.k_adresi.focus_set()

        self.sifre = Entry(p, width=25)
        self.sifre.place(x=220, y=130)

        giris_btn = Button(p, text=u"Giri� Yap", command = self.giris)
        giris_btn.place(x=270, y=180)
        

        cikis_btn = Button(p, text=u"��k��", command=pencere.destroy)
        cikis_btn.place(x=200, y=180)


    def giris(self, event=None):
        self.k = self.k_adresi.get()
        s = self.sifre.get()
        
        self.baglanti = smtplib.SMTP_SSL("smtp.gmail.com", "465")
        try:
            self.baglanti.login(self.k,s)
            self.bilgi["text"] = u"Giri� ba�ar�l�"
            self.bilgi["fg"] = "green"
            pencere.destroy()
            self.ileti_pen()            
            
        except:
            self.bilgi["text"] = u"L�tfen bilgilerinizi ve ba�lant�n�z� kontrol ediniz."
            self.bilgi["fg"] = "red"


    def ileti_pen(self):
        p = Tk()
        p.resizable(width = False, height = False)
        p.geometry("700x500+350+100")
        p.title(u"...�leti Paneli...")
        p.bind("<Return>", self.gonder)

        alici = Label(p, text=u"Al�c� :")
        alici.place(x=10, y=10)
        alici.focus_set()

        self.alici_adresi = Entry(p, width=50)
        self.alici_adresi.place(x=60, y=10)

        ileti_k = Label(p, text=u"�letiniz :")
        ileti_k.place(x=10, y=40)

        self.ileti = Text(p)
        self.ileti.place(x=60, y=40, relheight=0.879, relwidth=0.9)

        gonder_btn = Button(p, text=u"G�nder", command =self.gonder)
        gonder_btn.place(x=630, y=8)

        self.drm_cubugu = Label(p, text=u"�letinizi giriniz.")
        self.drm_cubugu.place(x=620, y=480)


        p.mainloop


    def gonder(self, event=None):
        a = self.alici_adresi.get()
        m = self.ileti.get(1.0,END)        
        try:
            self.baglanti.sendmail(self.k, a, m)
            self.baglanti.quit()
            self.drm_cubugu["text"] = u"�letiniz g�nderildi."
            self.drm_cubugu["fg"] = "green"
            self.drm_cubugu.place(x=590, y=480)

        except:
            self.drm_cubugu["text"] = u"�letiniz g�nderilemedi."
            self.drm_cubugu["fg"] = "red"
            self.drm_cubugu.place(x=580, y=480)
            
        




pencere = Tk()
pencere.geometry("500x300+500+200")



p = Pencere()


pencere.mainloop()
