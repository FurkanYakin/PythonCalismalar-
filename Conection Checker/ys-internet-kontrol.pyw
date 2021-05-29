# ys_internet_kontrol.py

"""
Betik çalıştırıldığında periyodik olarak internet
bağlantısını kontrol edecek ve bağlantı kurulunca
sesli olarak uyaracak

"""

from urllib.request import urlopen
from time import sleep,time
#from subprocess import call
import random
import requests
import pyttsx3

BAGLAN = ["https://www.google.com","https://www.ibm.com"]
UYU = 5
PRINT_EXCEPTION = False

def getUrl():
    return random.choice(BAGLAN)

def internet_kontrol():
    try:
        _ = requests.get(getUrl(),timeout=5)
        return True, None
    except Exception as e:
        return False, e

def internet_kontrol2():
    try:
        urlopen(getUrl())
        return True, None
    except Exception as e:
        return False, e

def speak_it(cumle):
    engine.setProperty('rate',150)  # kelime / dakika
    engine.setProperty('volume',1.0)  # sesin yüksekliği
    engine.say(cumle)
    engine.runAndWait()
    

if __name__ == "__main__":
    engine = pyttsx3.init()
    t = time()
    
    var=0
    yok=0
    while True:
      #  print(f"{time() - t:.2f}", end=' ', flush=True)
        chk, e = internet_kontrol()
        # chk, e = internet_kontrol2()
        if chk:
            var+=1
            if var==1:
                yok=0
                cumle = "CONNECTED!"
                speak_it(cumle)
              #  call(["espeak", "-v", "en+f3", cumle])
              #  print("İnternet bağlantısı kuruldu!")
            
            else:
                pass

            
        else:
            yok+=1
            if yok==1:
                var=0
                cumle = "CONNECTION BROKED!"
                speak_it(cumle)
              #  call(["espeak", "-v", "en+f3", cumle])
                
          #  print(cumle)
                
            
            if PRINT_EXCEPTION:
                print(f"hata: {e}")
                
        sleep(UYU)
