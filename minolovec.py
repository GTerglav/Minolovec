import bottle, model

minolovec = model.Minolovec()

@bottle.get("/")
def prva_stran():
    minolovec = 'img10.png'
    return bottle.template("index.tpl", picture = minolovec)

@bottle.route('/<img10.png>')
def serve_pictures(picture):
    return static_file(picture, root='/img10.png')

@bottle.post("/igra/")
def zacni_novo_igro():
    # Naredi novo igro
    niz = str(bottle.request.forms.getunicode("velikost_mine"))
    if niz == "":
        pass
    else:
        sez = niz.split(" ")
        velikost = sez[0]
        mine = sez[1]
    id_igre = minolovec.nova_igra(velikost = "9", mine = "10")
    # Preusmeri na naslov za igranje nove igre
    bottle.redirect("/igra/{}/".format(id_igre))
    return

@bottle.get("/igra/<id_igre:int>/")
def prikazi_igro(id_igre):
    (igra, poskus) = minolovec.igre[id_igre]
    return bottle.template("igra.tpl", igra=igra, id_igre = id_igre, poskus = poskus)

@bottle.post("/igra/<id_igre:int>/")
def ugibaj_crko(id_igre):
    ugib = bottle.request.forms.getunicode("poskus")
    minolovec.ugibaj(id_igre, ugib)
    bottle.redirect("/igra/{}/".format(id_igre))
    return

bottle.run(debug = True, reloader = True)