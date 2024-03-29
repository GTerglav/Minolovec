import model

NAVODILA = "Cilj igre je odkriti vsa polje kjer ni min. \nPred začetkom izberemo velikost polja n x n z vpisom ene številke, ki predstavlja n. Enako storimo za število min. \nPolje odkriješ tako da najprej vpišeš vrstico, nato pa še stolpec (Primer: 3 4). \nPolje lahko označiš tudi z zastavico, tako da na koncu dodaš še f (Primer 3 4 f)"


def pozdrav():
    return input("Dobrodošli v minolovca! Za pomoč vpišite črko h ali pa vpišite velikost polja :")

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

def izpis_napake():
        return "Nepravilen vnos, poskusite še enkrat"

def izpis_zmage(igra):
    return "Čestitamo, pravilno ste rešili polje!"

def izpis_poraza(igra):
    return "Ha ha, idiot, razneslo te je" 

def zahtevaj_vnos():
    return input("Napiši vrstico in stolpec, loči ju s presledkom:")

def novo_polje():
    return input("Napiši velikost polja:")

def nove_mine():
    return input("Napiši število min:")

def zazeni_umesnik():
        velikost = pozdrav()
        if velikost == "h":
                print(NAVODILA)
                zazeni_umesnik()
        else:
                pass
        mine = nove_mine()
        if mine == "h":
                print(NAVODILA)
                zazeni_umesnik()
        else:
                pass
        
        if model.nova_igra(velikost, mine) == "F":
                print(izpis_napake())
                zazeni_umesnik()
        else:
                igra = model.nova_igra(velikost, mine)

                while True:

                        print(izpis_igre(igra))

                        poskus = zahtevaj_vnos()

                        if igra.ugibaj(poskus) == "F":
                               print(izpis_napake())
                        
                        if poskus == "h":
                                print(NAVODILA)
                        
                        if igra.poraz():
                                print(izpis_igre(igra))
                                print(izpis_poraza(igra))
                                info = novo_polje()
                                info2 = nove_mine()
                                if model.nova_igra(info, info2) == "F":
                                        print(izpis_napake())
                                        zazeni_umesnik()
                                else:
                                        igra = model.nova_igra(info, info2)

                        elif igra.zmaga():
                                print(izpis_igre(igra))
                                print(izpis_zmage(igra))
                                info = novo_polje()
                                info2 = nove_mine()
                                if model.nova_igra(info, info2) == "F":
                                        print(izpis_napake())
                                        zazeni_umesnik()
                                else:
                                        igra = model.nova_igra(info, info2)

                return

zazeni_umesnik()