
#-*-coding:cp1254-*-
from __future__ import division
import random
print """
Bu programcik Furkan YAKIN tarafindan hazirlanmistir.
Bu programcikla hesap yapabilir oyun oynayabilirsiniz."""

print """
1...Kayit ol
2...Giris
"""


"""Yapmak istediklerimiz:
1...4 işlem haricinde kare alma, mod alma... gibi işlemleri yapabilen bir hesap makinesi
2...Bir kahraman ve düşmanların oldugu vurulabilen askerlerden oluşan bir oyun
3...Bunlara birde kayıt olan kişilerin girebilmesini istiyoruz
"""


class hesap_makinesi():
    def toplama(self, a, b):
        print a, "+", b, "=", a+b

    def cikarma(self, a, b):
        print a, "-", b, "=", a-b

    def carpma(self, a, b):
        print a, "x", b, "=", a*b

    def bolme(self, a, b):
        print a, "/", b, "=", a/b

    def kare_alma(self, a, b):
        print a, "ussu" , b, " = ", a**b

    def mod_alma(self, a, b):
        print a, "/", b, " bolumunden kalan = ", a%b


class sifreleme():
    def kayit_ol(self):
        print "=============Kayit Ekrani============"
        dosya = open("kullanıcılar.txt", "r")
        giris_kullanici_adi = raw_input("Kullanici adi: ")
        giris_sifre = raw_input("Sifre: ")

        kullanici_adlari = []

        for satir in dosya.readlines():
            kullanici_adi, sifre = satir.split()
            kullanici_adlari.append(kullanici_adi)


        if giris_kullanici_adi in kullanici_adlari:
            print """==========================================================
Girmis oldugunuz kullanici adi kullanimdadir.
Lutfen yeni bir kullanici adi giriniz."""
            self.kayit_ol()


        else:

            while True:
                if len(giris_sifre) < 6:
                    print "Sifreniz en az 6 haneli olmalidir."
                    giris_sifre = raw_input("Sifre: ")
                    continue
                
                else:
                    dosya = open("kullanıcılar.txt", "a")
                    dosya.write("\n%s  %s"%(giris_kullanici_adi, giris_sifre))
                    dosya.close()
                    break

        dosya.close()
            

    def giris(self):
        print "=============Giris Ekrani============"
        giris_kullanici = raw_input("Kullanici adi: ")
        giris_sifre = raw_input("Sifre: ")
        dosya = open("kullanıcılar.txt")
        kullanicilar = {"kullanici_adi": "sifre" }
        kullanici_adlari = []
        for satir in dosya.readlines():
            kullanici_adi, sifre = satir.split()

            kullanicilar[kullanici_adi] = sifre
            kullanici_adlari.append(kullanici_adi)


        if giris_kullanici in kullanici_adlari:
            if kullanicilar[giris_kullanici] == giris_sifre:
                print "HOSGELDINIZ"

            else:
                print "Hatali bir parola girdiniz."
                self.giris()

        else:
            print "Lutfen once kayit olunuz."
            self.kayit_ol()
            self.giris()

        dosya.close()
                

class asker():
    def __init__(self):
        self.guc = 100
        self.silah = 50

    def vurulma(self, vurma):
        self.guc -= vurma

    def canlimi(self):
        if self.guc <= 0:
            return False
        else:
            return True



class kahraman(asker):
    def __init__(self):
        self.guc = 2000
        self.silah = 80


class dusman(asker):
    def __init__(self):
        self.guc = random.randint(60, 120)
        self.silah = random.randint(20, 120)
        
        
    


        

sifreleme = sifreleme()
while True:
    sor = raw_input("Lutfen islem seciniz: ")
    if sor == "1":
        sifreleme.kayit_ol()
        sifreleme.giris()
        break
    
    elif sor == "2":
        sifreleme.giris()
        break

    else:
        continue



print """
1...Hesap Makinesi
2...Basit bir oyun"""

sor = raw_input("Seciniz: ")

if sor == "1":
    hm = hesap_makinesi()
    while True:
        print """==========================================================
ONEMLİ NOT = Isleminizi yazarken arada bosluk birakiniz (12 + 5 gibi)
NOT = Us almak icin ** i kullanin.
NOT = Mod almak icin % i kullanin."""
        islem = raw_input("Islem giriniz: ")
        
        if islec == "+":
            print "=========================================================="
            hm.toplama(int(sayi1), int(sayi2))

        elif islec == "-":
            print "=========================================================="
            hm.cikarma(int(sayi1), int(sayi2))

        elif islec == "*":
            print "=========================================================="
            hm.carpma(int(sayi1), int(sayi2))

        elif islec == "/":
            print "=========================================================="
            hm.bolme(int(sayi1), int(sayi2))

        elif islec == "**":
            print "=========================================================="
            hm.kare_alma(int(sayi1), int(sayi2))

        elif islec == "%":
            print "=========================================================="
            hm.mod_alma(int(sayi1), int(sayi2))

        else:
            break




if sor == "2":
    kahraman = kahraman()

    dusmanlar = []
    
    for i in range(10):
        dusmanlar.append(dusman())


    while kahraman.canlimi() and len(dusmanlar) > 0:

        print "Kahramanin cani: ", kahraman.guc

        for sayi, dusman in enumerate(dusmanlar):
            print sayi+1, "Nolu dusmanin cani: ", dusman.guc, "   Silahi: ", dusman.silah


        hedef = raw_input("Dusmanininizi seciniz: ")        

        if hedef == "":
            continue

        dusmanlar[int(hedef)-1].vurulma(kahraman.silah)

        for dusman in dusmanlar:
            if dusman.guc <= 0:
                del dusmanlar[dusmanlar.index(dusman)]

        for i in range(random.randint(1, len(dusmanlar))):
            kahramani_vuran = random.choice(dusmanlar)
            kahraman.vurulma(kahramani_vuran.silah)
              

        if len(dusmanlar) <= 0:
            print "Kazandiniz."
            break
        
        elif kahraman.guc <= 0:
            print "Kahramanimiz oldu."
            break

        else:
            continue
            

        
    
    

    



