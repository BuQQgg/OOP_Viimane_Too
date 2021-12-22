'''
Mäng
12/20/2021
Kevin Kiisk
'''



class Karakter:
    
    def __init__(self, nimi, elud, tugevus):
        self.nimi = nimi
        self.elud = elud
        self.tugevus = tugevus

    def kaotaElusi(self, kaotaElud):
        self.elud = self.elud - kaotaElud

class Vaenlane:
    
    def __init__(self, elud, tugevus):
        self.elud = elud
        self.tugevus = tugevus

    def kaotaElusi(self, kaotaElud):
        self.elud = self.elud - kaotaElud
            
from easygui import *    
            
nimi = enterbox("Tere kuidas on teie nimi?")
if nimi == None:
    msgbox("Palun sisesta korrektne nimi!!")
else:
    msgbox("Tere, " + nimi +"! " + "Olete sattunud labürinti. Teil on 100 elu, kui satute kokku vaenlastega kaotad 50 elu aga kui teed õiged valikud jõuad õnnelikult lõppu.")