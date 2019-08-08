import random




#Konstante


class Celica:
        def __init__(self, mina, vidna=False, zastavica=False):
                self.mina = mina
                self.vidna = vidna
                self.zastavica = zastavica
                return

        def __repr__(self):
                if self.mina == False and self.vidna == True and self.zastavica == False:
                        return "H"
                if self.vidna == False:
                        return "O"
                if self.vidna == True and self.zastavica == True:
                        return "F"
                if self.vidna == True and self.mina == True:
                        return "X"


        
        def razkrij(self):
                self.vidna = True
                return
        
        def postavi_zastavico(self):
                if not self.vidna:
                        self.zastavica = not self.zastavica
                return

        def postavi_mino(self):
                self.mina = True
                return


class Polje:
        def __init__(self, seznam):
                self.seznam = seznam
        
        def poraz(self):
                for i in range(len(self.seznam)):
                        for j in self.seznam[i]:
                                if j.mina == True and j.vidna == True:
                                        return True
                return False


def naredi_polje(velikost, mine):
        #naredi matriko
        if mine > velikost ** 2:
                return False
        matrika = []
        for i in range(velikost):
                vrstica = []
                for j in range(velikost):
                        vrstica.append(Celica(False))
                matrika.append(vrstica)
        
        polje = Polje(matrika)
        
        #postavi mine
        sez_moznosti = []
        for i in range(velikost):
                for j in range(velikost):
                        sezz = []
                        sezz.append(i)
                        sezz.append(j)
                        sez_moznosti.append(sezz)

        for i in range(mine):
                nov_poz = random.choice(sez_moznosti)
                sez_moznosti.remove(nov_poz)
                matrika[nov_poz[0]][nov_poz[1]].postavi_mino()
        return matrika
        



