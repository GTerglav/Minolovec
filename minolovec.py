import bottle, model

@bottle.get("/")
def prva_stran():
    minolovec = 'img10.png'
    return bottle.template("index.tpl", picture = minolovec)

@bottle.route('/<img10.png>')
def serve_pictures(picture):
    return static_file(picture, root='/img10.png')

@bottle.post("/igra/<id_igre:int>/")
def nova_igra(id_igre):
    velikost = bottle.request.forms.getunicode("velikost")
    mine = bottle.request.forms.getunicode("mine")
    igra = model.nova_igra(velikost, mine)

    #bottle.redirect("/igra/{}/".format(id_igre))
    return model.izpis_igre(igra)


bottle.run(debug = True, reloader = True)