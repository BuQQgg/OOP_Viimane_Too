'''
Mäng
22/12/2021
Kevin Kiisk ja Merle Luht
'''
class Karakter:
 
    def __init__(self,nimi,elud,tugevus):
        self.nimi = nimi
        self.elud = elud
        self.tugevus = tugevus
        
    def kaotaElusid(self,kaotatudElud):
        self.elud = self.elud - 1
        if self.elud < 0:
            print("Kõik elud kaotatud.")
        else:
            print("Sul on :", self.elud, "elu.")
    def lisaElusid(self,lisatudElud):
        self.elud = self.elud + lisatudElud
        print("Sul on:", self.elud, "elu.")
    
    def setNimi(self,nimi):
        self.nimi = nimi
      
class Vaenlane:
    
    def __init__(self,elud,tugevus):
        self.elud = elud
        self.tugevus = tugevus

    def kaotaElusid(self,kaotatudElud):
        self.elud = self.elud - 1
        if self.elud < 0:
            print("Kõik elud kaotatud.")
        else:
            print("Vaenlasel on :", self.elud, "elu.")
        
tegelane1 = Karakter("Tegelane1",100,10)
vaenlane1 = Vaenlane(100,50)
#tegelane1.kaotaElusid(20)
#tegelane1.lisaElusid(10)
#vaenlane1.kaotaelusi()

print(tegelane1.elud, vaenlane1.elud)
#tegelane1.setNimi("...")

from easygui import *

while True:

    
    valikud = ["Üles","Alla","Paremale","Vasakule"]
    valikud1 = ["Üles","Alla","Paremale","Vasakule"]
    mangijaValik = buttonbox("Tee valik, kuhu soovid liikuda:", choices = valikud)
    msgbox(f"\nValisid {mangijaValik}\n")
    mangijaTeineValik = buttonbox("Tee valik, kuhu soovid edasi liikuda:", choices = valikud1)
    msgbox(f"\nValisid {mangijaTeineValik}\n")
    if mangijaTeineValik == "Vasakule":
        msgbox("Sattusid vaenlase ruutu, kaotad 50 elu!")
    elif mangijaTeineValik == "Paremale":
        msgbox("Ok!")
    elif mangijaTeineValik == "Üles":
        msgbox("Ok!")
    elif mangijaTeineValik == "Alla":
        msgbox("Ok!")
    mangijaKolmasValik = buttonbox("Tee valik, kuhu soovid edasi liikuda:", choices = valikud1)
    msgbox(f"\nValisid {mangijaKolmasValik}\n")
    if mangijaKolmasValik == "Paremale":
        msgbox("Sattusid vaenlase ruutu, kaotad 50 elu!")
        if mangijaKolmasValik == "Paremale" and mangijaTeineValik == "Vasakule":
            msgbox("Oled kaotanud kõik elud!")
            exit()
    elif mangijaKolmasValik == "Vasakule":
        msgbox("Ok!")
    elif mangijaKolmasValik == "Üles":
        msgbox("Ok!")
    elif mangijaKolmasValik == "Alla":
        msgbox("Ok!")
    mangijaNeljasValik = buttonbox("Tee valik, kuhu soovid edasi liikuda:", choices = valikud1)
    msgbox(f"\nValisid {mangijaNeljasValik}\n")
    if mangijaNeljasValik == "Üles":
        msgbox("Sattusid vaenlase ruutu, kaotad 50 elu!")
        if mangijaNeljasValik == "Üles" and mangijaTeineValik == "Vasakule":
            msgbox("Oled kaotanud kõik elud!")
            exit()
        elif mangijaNeljasValik == "Üles" and mangijaKolmasValik == "Paremale":
            msgbox("Oled kaotanud kõik elud!")
            exit()
    elif mangijaNeljasValik == "Vasakule":
        msgbox("Ok!")
    elif mangijaNeljasValik == "Üles":
        msgbox("Ok!")
    elif mangijaNeljasValik == "Alla":
        msgbox("Ok!")
    mangijaViiesValik = buttonbox("Tee valik, kuhu soovid edasi liikuda:", choices = valikud1)
    msgbox(f"\nValisid {mangijaViiesValik}\n")
    if mangijaViiesValik == "Üles":
        msgbox("Sattusid vaenlase ruutu, kaotad 50 elu!")
        if mangijaViiesValik == "Üles" and mangijaNeljasValik == "Üles":
            msgbox("Oled kaotanud kõik elud!")
            exit()
        if mangijaViiesValik == "Üles" and mangijaTeineValik == "Vasakule":
            msgbox("Oled kaotanud kõik elud!")
            exit()
        elif mangijaViiesValik == "Üles" and mangijaKolmasValik == "Paremale":
            msgbox("Oled kaotanud kõik elud!")
            exit()
    elif mangijaViiesValik == "Vasakule":
        msgbox("Oled edukalt jõudnud labürindi lõppu, palju õnne!")
    elif mangijaViiesValik == "Üles":
        msgbox("Oled edukalt jõudnud labürindi lõppu, palju õnne!")
    elif mangijaViiesValik == "Alla":
        msgbox("Oled edukalt jõudnud labürindi lõppu, palju õnne!")
    kordus = enterbox("Uus mäng? (y/n): ")
    if kordus.lower() != "y":
        break    