import random




#Konstante

#polje 9*9
rešeno_polje9 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]


class Celica:
        def __init__(self, vrsta_id, stolpec_id, mina=False, vidna=False, zastavica=False):
                self.vrsta = vrsta
                self.stolpec = stolpec
                self.mina = mina
                self.vidna = vidna
                self.zastavica = zastavica
                return

        def razkrij(self):
                self.vidna = True
                return
        
        def postavi_zastavico(self):
                if not celica.vidna:
                        self.zastavica = not self.zastavica
                return

        def postavi_mino(self):
                self.mina = True
                return


class Polje:

        def __init__(self, velikost):
                self.velikost = velikost
                return


        def mina_repr(self, vrsta_id, stolpec_id):
                cell = self[vrsta_id][stolpec_id]


class Igra:
        
        




def naredi_mino(sez):
    vrstica = random.randint(0,8)
    stolpec = random.randint(0,8)
    if not rešeno_polje9[vrstica][stolpec] == "*":
        rešeno_polje9[vrstica][stolpec] = "*"


def postavi_mine(self):
    for n in range(10):
        naredi_bombo(rešeno_polje9)

        





reset()