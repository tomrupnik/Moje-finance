import bottle
from model import *


finance = Finance([], [], "prihodki.json", "stroski.json")
finance.nalozi_prihodke()
finance.nalozi_stroske()


@bottle.get("/")
def osnovna_stran():
    return bottle.template("osnovna.tpl")


@bottle.post("/dodaj_prihodek/")
def dodaj_p():
    return bottle.template("vnos_prihodka.tpl")


@bottle.post("/dodaj_prihodek/dodaj")
def pomozna1():
    namen = bottle.request.forms.get("namen")
    znesek = bottle.request.forms.get("vrednost")
    mesec = bottle.request.forms.get("mesec")
    prihodek = Prihodek(namen, znesek, mesec)
    finance.dodaj_prihodek(prihodek)
    finance.zapisi_prihodke()
    bottle.redirect("/")


@bottle.post("/dodaj_strosek/")
def dodaj_s():
    return bottle.template("vnos_stroska.tpl")


@bottle.post("/dodaj_strosek/dodaj")
def pomozna2():
    namen = bottle.request.forms.get("namen")
    znesek = bottle.request.forms.get("vrednost")
    mesec = bottle.request.forms.get("mesec")
    strosek = Strosek(namen, znesek, mesec)
    finance.dodaj_strosek(strosek)
    finance.zapisi_stroske()
    bottle.redirect("/")


@bottle.post("/izpisi_stroske/")
def izpis_stroskov():
    return bottle.template("izpisi_stroske.tpl")


@bottle.post("/izpisi_stroske/vsi_stroski")
def izpisi_stroske():
    return finance.izpisi_stroske()


@bottle.post("/izpisi_stroske/izpisi_stroske_mesec")
def za_mesec1():
    mesec = bottle.request.forms.get("mesec")
    return finance.izpisi_stroske_meseci(mesec)


@bottle.post("/izpisi_prihodke/")
def izpis_prihokov():
    return bottle.template("izpisi_prihodke.tpl")


@bottle.post("/izpisi_prihodke/vsi_prihodki")
def izpisi_prihodke():
    return finance.izpisi_prihodke()


@bottle.post("/izpisi_prihodke/izpisi_prihodke_mesec")
def za_mesec2():
    mesec = bottle.request.forms.get("mesec")
    return finance.izpisi_prihodke_meseci(mesec)


@bottle.post("/izpis_stanja/")
def stan():
    return bottle.template("izpis_stanja.tpl")


@bottle.post("/izpis_stanja/celotno_stanje")
def celotno():
    return str(finance.izpis_stanja()) + " evrov"


@bottle.post("/izpis_stanja/izpisi_stanje_mesec")
def stanje_mesec():
    mesec = bottle.request.forms.get("mesec")
    return str(finance.izpis_stanja_mesec(mesec)) + " evrov"


bottle.run(debug=True, reloader=True)
