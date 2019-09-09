
import json

meseci = ["januar", "februar", "marec", "april", "maj", "junij",
          "julij", "avgust", "september", "oktober", "november", "december"]


class Prihodek:

    def __init__(self, vir, znesek, mesec,):
        self.znesek = znesek
        self.mesec = mesec
        self.vir = vir

    def __str__(self):
        return "{}: {}€, {}".format(self.vir, self.znesek, self.mesec)

    def __lt__(self, other):
        return (meseci.index(self.mesec) < meseci.index(other.mesec))


class Strosek:

    def __init__(self, namen, znesek, mesec):
        self.znesek = znesek
        self.mesec = mesec
        self.namen = namen

    def __str__(self):
        return "{}: {}€, {}".format(self.namen, self.znesek, self.mesec)

    def __lt__(self, other):
        return (meseci.index(self.mesec) < meseci.index(other.mesec))


class Finance:
    def __init__(self, sez_prihodki, sez_stroski, datoteka_prihodkov, datoteka_stroski):
        self.sez_prihodki = sez_prihodki
        self.sez_stroski = sez_stroski
        self.datoteka_prihodkov = datoteka_prihodkov
        self.datoteka_stroski = datoteka_stroski

    def dodaj_prihodek(self, prihodek):
        self.sez_prihodki.append(prihodek)

    def izpisi_prihodke(self):
        prikaz = ""
        self.sez_prihodki.sort()
        for prihodek in self.sez_prihodki:
            prikaz += ("<br>" + str(prihodek) + "</br>")
        return prikaz

    def izpisi_prihodke_meseci(self, mesec):
        prikaz = ""
        for prihodek in self.sez_prihodki:
            if prihodek.mesec == mesec:
                prikaz += ("<br>" + str(prihodek) + "</br>")
        return prikaz

    def dodaj_strosek(self, strosek):
        self.sez_stroski.append(strosek)

    def izpisi_stroske(self):
        prikaz = ""
        self.sez_stroski.sort()
        for strosek in self.sez_stroski:
            prikaz += ("<br>" + str(strosek) + "</br>")
        return prikaz

    def izpisi_stroske_meseci(self, mesec):
        prikaz = ""
        for strosek in self.sez_stroski:
            if strosek.mesec == mesec:
                prikaz += ("<br>" + str(strosek) + "</br>")
        return prikaz

    def zapisi_prihodke(self):
        with open(self.datoteka_prihodkov, "w") as f:
            vsi_prihodki = []
            for prihodek in self.sez_prihodki:
                prihodek_dic = {"vir": prihodek.vir,
                                "znesek": prihodek.znesek, "mesec": prihodek.mesec}
                vsi_prihodki.append(prihodek_dic)
            json.dump(vsi_prihodki, f)

    def nalozi_prihodke(self):
        with open(self.datoteka_prihodkov, "r") as f:
            prihodki_dat = json.load(f)
            for prihodek_dic in prihodki_dat:
                self.sez_prihodki.append(Prihodek(prihodek_dic["vir"], prihodek_dic["znesek"],
                                                  prihodek_dic["mesec"]))

    def zapisi_stroske(self):
        with open(self.datoteka_stroski, "w") as f:
            vsi_stroski = []
            for strosek in self.sez_stroski:
                stroski_dic = {"namen": strosek.namen,
                               "znesek": strosek.znesek, "mesec": strosek.mesec}
                vsi_stroski.append(stroski_dic)
            json.dump(vsi_stroski, f)

    def nalozi_stroske(self):
        with open(self.datoteka_stroski, "r") as f:
            stroski_dat = json.load(f)
            for stroski_dic in stroski_dat:
                self.sez_stroski.append(Strosek(stroski_dic["namen"], stroski_dic["znesek"],
                                                stroski_dic["mesec"]))

    def izpis_stanja(self):
        prihodki = 0
        stroski = 0
        for prihodek in self.sez_prihodki:
            prihodki += int(prihodek.znesek)
        for strosek in self.sez_stroski:
            stroski += int(strosek.znesek)
        return prihodki - stroski

    def izpis_stanja_mesec(self, mesec):
        prihodki = 0
        stroski = 0
        for prihodek in self.sez_prihodki:
            if prihodek.mesec == mesec:
                prihodki += int(prihodek.znesek)
        for strosek in self.sez_stroski:
            if strosek.mesec == mesec:
                stroski += int(strosek.znesek)
        return prihodki - stroski
