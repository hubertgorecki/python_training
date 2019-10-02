class Contact:

    def __init__(self, imie=None, imie2=None, nazwisko=None, inicjaly=None, firma=None, zwrot=None, adres=None,
                 tel_domowy=None, tel_komorkowy=None, tel_praca=None,
                 adres_mail=None, adres_mail2=None, strona_domowa=None, dzien_urodzin=None, miesiac_urodzin=None,
                 rok_urodzenia=None,
                 alrternatywny_adres=None, id=None):
        self.imie = imie
        self.imie2 = imie2
        self.nazwisko = nazwisko
        self.inicjaly = inicjaly
        self.firma = firma
        self.zwrot = zwrot
        self.adres = adres
        self.tel_domowy = tel_domowy
        self.tel_komorkowy = tel_komorkowy
        self.tel_praca = tel_praca
        self.adres_mail = adres_mail
        self.adres_mail2 = adres_mail2
        self.strona_domowa = strona_domowa
        self.dzien_urodzin = dzien_urodzin
        self.miesiac_urodzin = miesiac_urodzin
        self.rok_urodzenia = rok_urodzenia
        self.alrternatywny_adres = alrternatywny_adres
        self.id = id
