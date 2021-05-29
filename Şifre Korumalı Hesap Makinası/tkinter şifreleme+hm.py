# -*- coding:cp1254 -*-
from Tkinter import*

def yaz(event = None):    
    exec "cozum = "+islem.get()
    sonuc.config(text = str(cozum), wraplength=350, fg = "blue", font = "courel 15 bold")
    islem.delete(0,END)        
def hm():
    global islem, sonuc
    
    pen = Tk()
    pen.title(u"Hesap Makinesi")
    pen.geometry("350x350+200+200")

    yazi = Label(text = u"Hoşgeldiniz", fg = "blue", font = "15")
    yazi.pack()

    islem = Entry()
    islem.pack(ipadx = 10, pady = 6)
    islem.focus_set()

    buton = Button(text = u"Hesapla", command = yaz)
    buton.pack(pady = 7)

    sonuc = Label(text = u"Bir işlem giriniz", font = "20", fg = "red")
    sonuc.pack(pady = 8)

    cikis = Button(text = u"Çıkış", command = pen.destroy)
    cikis.pack()

    pen.bind("<Return>", yaz)
    pen.bind("<Escape>", lambda event = None: pen.destroy())

    pen.mainloop()


def kayit_ol():    
    dosya = open("kullanıcılar.txt", "r")
    kullaniciadim = kullaniciadi.get()
    sifrem = sifre.get()
    
    kullanici_adlari = []

    for satir in dosya.readlines():
            kullanici_adi, sifres = satir.split()
            kullanici_adlari.append(kullanici_adi)


    if kullaniciadim in kullanici_adlari:
            yazi = Label(pencere)
            yazi.config(text = """Girmis oldugunuz kullanici adi kullanimdadir.
Lutfen yeni bir kullanici adi giriniz.""", fg = "RED")
            yazi.pack()

            kayit_ol



    else:
        while True:
            if len(sifrem) < 6:
                yazi = Label(pencere)
                yazi.config(text = "Sifreniz en az 6 haneli olmalidir.", fg = "RED")
                yazi.pack()
                
                break
                
            else:
                dosya = open("kullanıcılar.txt", "a")
                dosya.write("\n%s  %s"%(kullaniciadim, sifrem))
                dosya.close()

                yazi = Label(pencere)
                yazi.config(text = u"Kaydınız başarılı.", fg = "BLUE")
                yazi.pack()
                
                break

    dosya.close()



def giris(event = None):    
    dosya = open("kullanıcılar.txt")
    kullaniciadim2 = kullaniciadi.get()
    sifrem2 = sifre.get()

    kullanicilar = {}
    kullanici_adlari = []

    for satir in dosya.readlines():
        kullanici_adi, sifres = satir.split()

        kullanicilar[kullanici_adi] = sifres
        kullanici_adlari.append(kullanici_adi)


    if kullaniciadim2 in kullanici_adlari:
        if kullanicilar[kullaniciadim2] == sifrem2:
            
            pencere.destroy()

            hm()


        else:
            yazi = Label(pencere)
            yazi.config(text = u"Hatali bir parola girdiniz.", fg = "RED")
            yazi.place(x = 271, y = 80)


    else:
        yazi = Label(pencere)
        yazi.config(text = u"Lütfen önce kayıt olunuz.", fg = "RED")
        yazi.place(x = 270, y = 80)
        




pencere = Tk()
pencere.title(u"Şifreleme")
pencere.geometry("700x600+100+100")

yazi = Label(pencere)
yazi.config(text = u"""
Bu programcik Furkan YAKIN tarafindan hazirlanmistir.
Bu programcikla hesap yapabilir, oyun oynayabilirsiniz.""", font = "courel 15 bold", fg = "BLUE")
yazi.place(x = 70, y = 1)


kullanici = Label(pencere)
kullanici.config(text = u"Kullanıcı Adı: ")
kullanici.place(x = 235, y = 100)

kullaniciadi = Entry(pencere)
kullaniciadi.place(x = 300, y = 100)
kullaniciadi.focus_set()

parola = Label(pencere)
parola.config(text = u"Şifre:")
parola.place(x = 265, y = 125)

sifre = Entry(pencere)
sifre.place(x = 300, y = 125)

giriss = Button(pencere)
giriss.config (text = u"Giriş", command = giris)
giriss.place(x = 280, y = 150)

kayit = Button(pencere)
kayit.config (text = u"Kayıt Ol", command = kayit_ol)
kayit.place(x = 320, y = 150)

cikis = Button(pencere)
cikis.config(text = u"Çıkış", command = pencere.quit)
cikis.place(x = 300, y = 180)       

pencere.bind("<Return>", giris)
pencere.bind("<Escape>", lambda event = None: pencere.quit())

mainloop()
