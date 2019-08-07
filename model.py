import random, time, copy




#Konstante

#polje 9*9
rešeno_polje9 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]


def naredi_dombo(sez):
    vrstica = random.randint(0,8)
    stolpec = random.randint(0,8)
    if not rešeno_polje9[vrstica][stolpec] == "*":
        rešeno_polje9[vrstica][stolpec] = "*"


def postavi_bombe(self):
    for n in range(10):
        naredi_bombo(rešeno_polje9)

        





reset()