
import model

def pozdrav():
    return input("Dobrodošli v minolovca! Napišite velikost polja :")

def izpis_igre(igra):
    niz = ""
    for vrsta in range(len(igra.seznam)):
            vrstica_niza = ""
            for stolpec in range(len(igra.seznam)):
                    vrstica_niza += str(prikaz_celice(igra, vrsta, stolpec)) + " "
            niz += vrstica_niza + "\n"
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

def izpis_zmage(igra):
    return "Čestitamo, pravilno ste rešili polje!"

def izpis_poraza(igra):
    return "Ha ha, idiot, razneslo te je" 

def zahtevaj_vnos():
    return input("Napiši vrstico in stolpec, loči ju s presledkom:")

def novo_polje():
    return input("Napiši velikost polja :")

def nove_mine():
    return input("Napiši  število min:")

def zazeni_umesnik():
    velikost = int(pozdrav())
    mine = int(nove_mine())
    igra = nova_igra(velikost, mine)



    while True:

            print(izpis_igre(igra))

            poskus = zahtevaj_vnos()
            igra.ugibaj(poskus)

            if igra.poraz():
                    print(izpis_poraza(igra))
                    info = int(novo_polje())
                    info2 = int(nove_mine())
                    igra = nova_igra(info, info2)
            
            elif igra.zmaga():
                    print(izpis_zmage(igra))
                    info = int(novo_polje())
                    info2 = int(nove_mine())
                    igra = nova_igra(info, info2)
                    
    return

zazeni_umesnik()