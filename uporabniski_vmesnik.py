import bottle
from model import *

finance = Finance([], [], "prihodki.json", "stroski.json")
finance.nalozi_prihodke()
finance.nalozi_stroske()


@bottle.get("/")
def pogovor_z_uporabnikom():
    while True:
        print("*******************************************")
        funkcionalnost = int(input(
            "Kaj zelis:\n 1. dodaj prihodek \n 2. dodaj strošek \n 3. prikazi prihodke"
            + " \n 4. prikaži stroške \n 5. izpis stanja \n 6. izpis stanja za mesec "
            + "\n 7. izhod \n vpiši številko"))
        if (funkcionalnost == 1):
            namen = input("Vir:")
            znesek = input("Znesek:")
            mesec = input("Mesec:")
            prihodek = Prihodek(namen, znesek, mesec,)
            finance.dodaj_prihodek(prihodek)
            finance.zapisi_prihodke()

        if funkcionalnost == 2:
            namen = input("Namen:")
            znesek = input("Znesek:")
            mesec = input("Mesec:")
            strosek = Strosek(namen, znesek, mesec)
            finance.dodaj_strosek(strosek)
            finance.zapisi_stroske()

        if funkcionalnost == 3:
            x = int(input(
                "Kaj zelis:\n 1. izpis vseh prihodkov \n 2. izpis prihodkov po mesecih"
                + "\n vpiši številko"))
            if x == 1:
                finance.izpisi_prihodke()
            if x == 2:
                mesec = input("Kateri mesec: ")
                finance.izpisi_prihodke_meseci(mesec)

        if funkcionalnost == 4:
            x = int(input(
                "Kaj zelis:\n 1. izpis vseh stroškov \n 2. izpis stroškov po mesecih"
                + "\n vpiši številko"))
            if x == 1:
                finance.izpisi_stroske()
            if x == 2:
                mesec = input("Kateri mesec: ")
                finance.izpisi_stroske_meseci(mesec)

        if funkcionalnost == 5:
            print(finance.izpis_stanja() + "€")

        if funkcionalnost == 6:
            mesec = input("Kateri mesec:")
            print(finance.izpis_stanja_mesec(mesec) + "€")

        if funkcionalnost == 7:
            break


bottle.run(debug=True, reloader=True)
