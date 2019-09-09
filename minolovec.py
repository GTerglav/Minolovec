import bottle, model

minolovec = model.Minolovec()

@bottle.get("/")
def prva_stran():
    return bottle.template("index.tpl")

@bottle.post("/igra/")
def zacni_novo_igro():
    # Naredi novo igro
    niz = str(bottle.request.forms.getunicode("velikost_mine"))
    if niz == "":
        return bottle.template("index.tpl", picture = minolovec)
    if len(niz.split(" ")) == 1:
        return bottle.template("index.tpl", picture = minolovec)
    else:
        sez = niz.split(" ")
        velikost = sez[0]
        mine = sez[1]
    id_igre = minolovec.nova_igra(velikost, mine)
    # Preusmeri na naslov za igranje nove igre
    bottle.redirect("/igra/{}/".format(id_igre))
    return

@bottle.get("/igra/<id_igre:int>/")
def prikazi_igro(id_igre):
    (igra, mine, poskus) = minolovec.igre[id_igre]
    return bottle.template("igra.tpl", igra=igra, mine = mine, id_igre = id_igre, poskus = poskus)

@bottle.post("/igra/<id_igre:int>/")
def ugibaj_crko(id_igre):
    ugib = bottle.request.forms.getunicode("poskus")
    minolovec.ugibaj(id_igre, ugib)
    bottle.redirect("/igra/{}/".format(id_igre))
    return

bottle.run(debug = True, reloader = True)