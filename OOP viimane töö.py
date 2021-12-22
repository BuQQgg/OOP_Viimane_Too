'''
Mäng
12/20/2021
Kevin Kiisk
'''

from easygui import

class Karakter:
     def __init__(self, nimi, elud, tugevus):
        self.nimi = nimi
        self.elud = elud
        self.tugevus = tugevus

    def kaotaElusi(self, elup):
        self.elud = self.elud - elup

class Vaenlane:
    def __init__(self, elud, tugevus):
        self.elud = elud
        self.tugevus = tugevus

    def kaotaElusi(self, elud):
        self.elud = self.elud - elud
            
            
            
            