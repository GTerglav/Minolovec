import random




#Konstante
ZMAGA = "W"
PORAZ = "L"
NAPAKA = "F"
ZACETEK = "S"
PRVI = "first"


class Celica:
        def __init__(self, vrsta, stolpec, mina, vidna=False, zastavica=False):
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
                global PRVI
                str(ugib)
                sez = ugib.split(" ")

                #pogoji za neveljaven input                
                if len(sez) == 1:
                        return NAPAKA
                elif not sez[0].isdigit():
                        return NAPAKA
                elif not sez[1].isdigit():
                        return NAPAKA
                
                vrstica = int(sez[0]) - 1
                stolpec = int(sez[1]) - 1

                if vrstica > len(self.seznam) - 1 or  stolpec > len(self.seznam) - 1:
                        return NAPAKA
                elif vrstica < 0 or stolpec < 0:
                        return NAPAKA       
                if len(sez) == 3:
                        if sez[2] == "F" or sez[2] == "f":
                                self.postavi_zastavico(vrstica, stolpec)
                        else:
                                return NAPAKA                                             
                if len(sez) == 2:
                        #Prvi ugib ne more biti mina razen ce so vsa polja pokrita z minami, vendar si v tem primeru že zmagovalec
                        if PRVI == "frist":
                                PRVI = "scnd"
                                celica = self.seznam[vrstica][stolpec]
                                if celica.mina == True:
                                        sez_moznosti = []
                                        for i in range(len(self.seznam)):
                                                for j in range(len(self.seznam)):
                                                        celica2 = self.seznam[i][j]
                                                        if celica2.mina == False:
                                                                sezz = []
                                                                sezz.append(i)
                                                                sezz.append(j)
                                                                sez_moznosti.append(sezz)
                                        if sez_moznosti == []:
                                                self.razkrij(vrstica, stolpec)
                                        else:
                                                nov_poz = random.choice(sez_moznosti)
                                                self.seznam[nov_poz[0]][nov_poz[1]].postavi_mino()
                                                celica.mina = False
                                                self.razkrij(vrstica, stolpec)
                                else:
                                        self.razkrij(vrstica, stolpec)
                        else:
                                self.razkrij(vrstica, stolpec)
                elif len(sez) >= 4:
                        return NAPAKA       
                if self.zmaga():
                        return ZMAGA
                if self.poraz():
                        return PORAZ


def naredi_polje(velikost, mine):
        #naredi matriko
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
#Funkcija ki ujame napake, nato pa le pokliče zgornjo funkcijo, ki naredi polje      
def nova_igra(velikost, mine):
        if not velikost.isdigit():
                return NAPAKA 
        if not mine.isdigit():
                return NAPAKA

        velikost = int(velikost)
        mine = int(mine) 

        if mine > velikost ** 2:
                return NAPAKA 
        else:
                polje = naredi_polje(velikost, mine)
                return Polje(polje)
#funkciji za prikaz igre v spletnem vmeniku
def izpis_igre(igra):

        niz = "    "
        for stolpec in range(len(igra.seznam)):
                if stolpec >= 9:
                        niz += str(stolpec + 1) + " "
                else:
                        niz += str(stolpec + 1) + "  "
        niz += "\n" * 2
        for vrsta in range(len(igra.seznam)):
                vrstica_niza = ""
                for stolpec in range(len(igra.seznam)):
                        vrstica_niza += str(prikaz_celice(igra, vrsta, stolpec)) + "  "

                if vrsta >= 9:
                        niz += str(vrsta + 1) + "  " + vrstica_niza + "\n"
                else:
                        niz += str(vrsta + 1) + "   " + vrstica_niza + "\n"
        
        return niz

def prikaz_celice(igra, vrsta, stolpec):
    celica = igra.seznam[vrsta][stolpec]
    if celica.mina == False and celica.vidna == True and celica.zastavica == False:
            if igra.preštej_mine(vrsta,stolpec) == 0:
                    return " "
            else:
                    return igra.preštej_mine(vrsta,stolpec)
    if celica.vidna == False and celica.zastavica == False:
            return "O"
    if celica.zastavica == True:
            return "F"
    if celica.vidna == True and celica.mina == True:
            return "X"

#funkcija prešteje zastavice in pove koliko min je še ostalo
def ostale(igra, mine):
        stevec = 0
        for vrsta in range(len(igra.seznam)):
                for stolpec in range(len(igra.seznam[vrsta])):
                        celica = igra.seznam[vrsta][stolpec]
                        if celica.zastavica == True:
                                stevec += 1
        if int(mine) - stevec >= 3:
                return "Ostalo ti je še {} min".format(int(mine) - stevec)
        if int(mine) - stevec == 2:
                return "Ostali sta ti še 2 mini!"
        if int(mine) - stevec == 1:
                return "Ostala ti je le še ena mina!"
        else:
                return "Za zmago odkrij ostala polja!"

        

#Razred za spletni vmesnik, po vzoru vislic

class Minolovec:

    def __init__(self):
        # V slovarju igre ima vsaka igra svoj ID
        # ID je celo število
        self.igre = {} 
        return 

    def prost_id_igre(self):
        if self.igre == {}:
            return 0
        else:
            # preverimo katero od prvih "n+1" števil
            # še ni uporabljeno za id "n" iger
            for i in range(len(self.igre) + 1):
                if i not in self.igre.keys():
                    return i
    
    def nova_igra(self, velikost, mine):
        global PRVI
        # naredi novo igro z naključnim geslom in jo shrani (ZACETEK, igra) v slovar z novim id
        nov_id = self.prost_id_igre()       
        self.igre[nov_id] = (nova_igra(velikost, mine), mine, ZACETEK)
        PRVI = "frist"
        return nov_id

    def ugibaj(self, id_igre, ugib):
        # Pridobi igro
        (igra, mine, poskus) = self.igre[id_igre]
        # Ugibaj
        nov_poskus = igra.ugibaj(ugib)
        # Shrani rezultat poskusa v slovar
        self.igre[id_igre] = (igra, mine, nov_poskus)
        return