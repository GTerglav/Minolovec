import random




#Konstante
ZMAGA = "W"
PORAZ = "L"
NAPAKA_ZASTAVICA = "S"

class Celica:
        def __init__(self, vrsta, stolpec, mina, vidna=False, zastavica=False):
                self.vrsta = vrsta
                self.stolpec = stolpec
                self.mina = mina
                self.vidna = vidna
                self.zastavica = zastavica
                return

        def __repr__(self):
                if self.mina == False and self.vidna == True and self.zastavica == False:
                        return "H"
                if self.vidna == False:
                        return "O"
                if self.zastavica == True:
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
        
        def razkrij(self, vrsta, stolpec):
                celica = self.seznam[vrsta][stolpec]
                if celica.zastavica == True:
                        return 
                if celica.vidna == False:
                        celica.razkrij()
                        if self.preštej_mine(vrsta, stolpec) == 0:
                                for x_os, y_os in self.sosedi(vrsta, stolpec):
                                        if self.je_dovoljena(x_os, y_os):
                                                self.razkrij(x_os, y_os)

                #če je polje že odkrito in število zastavic, ki ga obkroža ustreza številu min okoli polja, ta funkcija razkrije vsa sosednja neodkrita polja
                #if celica.vidna == True and self.preštej_mine(vrsta, stolpec) == self.preštej_zastavice(vrsta, stolpec):
                #        for x_os, y_os in self.sosedi(vrsta, stolpec):
                #                cell = self.seznam[x_os][y_os]
                #                if self.je_dovoljena(x_os, y_os) and cell.vidna == False and cell.zastavica == False:
                #                        cell.razkrij() 

        def postavi_zastavico(self, vrsta, stolpec):
                celica = self.seznam[vrsta][stolpec]
                if celica.vidna == False:
                        celica.postavi_zastavico()                               
        
        def poraz(self):
                for i in range(len(self.seznam)):
                        for j in self.seznam[i]:
                                if j.mina == True and j.vidna == True:
                                        return True
                return False

        def zmaga(self):
                for i in range(len(self.seznam)):
                        for j in self.seznam[i]:
                                if j.mina == False and j.vidna == False:
                                        return False
                return True
        
        #funkciji preštejeta sosednje zastavice in mine
        def preštej_zastavice(self, vrsta, stolpec):
                vsota = 0
                for x_os, y_os in self.sosedi(vrsta, stolpec):
                        if self.je_dovoljena(x_os, y_os):
                                if self.seznam[x_os][y_os].zastavica == True:
                                        vsota += 1
                return vsota

        def preštej_mine(self, vrsta, stolpec):
                vsota = 0
                for x_os, y_os in self.sosedi(vrsta, stolpec):
                        if self.je_dovoljena(x_os, y_os):
                                if self.seznam[x_os][y_os].mina == True:
                                        vsota += 1
                return vsota
        # pomožni funkciji za zgornji dve                               
        def sosedi(self, vrsta, stolpec):
                sez = []
                okolica = ((-1, -1), (-1,  0), (-1,  1),
                           (0 , -1),           (0 ,  1),
                           (1 , -1), (1 ,  0), (1 ,  1))
                for premik_x, premik_y in okolica:
                        sez.append((vrsta + premik_x, stolpec + premik_y))
                return sez 
        
        
        def je_dovoljena(self, vrsta, stolpec):
                return 0 <= vrsta <= len(self.seznam) - 1 and 0 <= stolpec <= len(self.seznam) - 1
        
        # funkcija ki sprejme naš ugib
        def ugibaj(self, ugib):
                str(ugib)
                sez = ugib.split(" ")
                vrstica = int(sez[0]) - 1
                stolpec = int(sez[1]) - 1
                if len(sez) == 3:
                        self.postavi_zastavico(vrstica, stolpec)
                else:
                        self.razkrij(vrstica, stolpec)

                

                if self.zmaga():
                        return ZMAGA
                elif self.poraz():
                        return PORAZ


def naredi_polje(velikost, mine):
        #naredi matriko
        if mine > velikost ** 2:
                return False
        matrika = []
        for i in range(velikost):
                vrstica = []
                for j in range(velikost):
                        vrstica.append(Celica(i, j, False))
                matrika.append(vrstica)
               
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
        
        polje = Polje(matrika)
        return matrika
        
def razkrij_vse(sez):
        for i in range(len(sez)):
                for j in range(len(sez)):
                        sez[i][j].razkrij()
        return

def nova_igra(velikost, mine):
        polje = naredi_polje(velikost, mine)
        return Polje(polje)



