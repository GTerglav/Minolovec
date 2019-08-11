import random




#Konstante


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

        
        
        def __str__(self):
                niz = ""
                for vrsta in range(len(self.seznam)):
                        vrstica_niza = ""
                        for stolpec in range(len(self.seznam)):
                                vrstica_niza += str(self.prikaz_mine(vrsta, stolpec)) + " "
                        niz += vrstica_niza + "\n"
                return niz 
        
        def prikaz_celice(self, vrsta, stolpec):
                celica = self.seznam[vrsta][stolpec]
                if celica.mina == False and celica.vidna == True and celica.zastavica == False:
                        return self.preštej_mine(vrsta,stolpec)
                if celica.vidna == False:
                        return "O"
                if celica.zastavica == True:
                        return "F"
                if celica.vidna == True and celica.mina == True:
                        return "X"
        
        def razkrij(self, vrsta, stolpec):
                celica = self.seznam[vrsta][stolpec]
                if celica.vidna == False:
                        celica.razkrij()
                        if self.preštej_mine(vrsta, stolpec) == 0:
                                for x_os, y_os in self.sosedi(vrsta, stolpec):
                                        if self.je_dovoljena(x_os, y_os):
                                                self.show(x_os, y_os)
        
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
        

        def preštej_mine(self, vrsta, stolpec):
                vsota = 0
                for x_os, y_os in self.sosedi(vrsta, stolpec):
                        if self.je_dovoljena(x_os, y_os):
                                if self.seznam[x_os][y_os].mina == True:
                                        vsota += 1
                return vsota

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


