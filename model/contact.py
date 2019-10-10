from sys import maxsize


class Contact:

    def __init__(self, imie=None, imie2=None, nazwisko=None, inicjaly=None, firma=None, zwrot=None, adres=None,
                 tel_domowy=None, tel_komorkowy=None, tel_praca=None, tel_fax=None,
                 wszystkie_tel_na_stronie_glownej=None, adres_mail=None, adres_mail2=None, adres_mail3=None, wszystkie_adresy_mail=None,
                 strona_domowa=None,
                 dzien_urodzin=None, miesiac_urodzin=None,
                 rok_urodzenia=None,
                 alrternatywny_adres=None, tel_domowy2=None, id=None):
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
        self.tel_fax = tel_fax
        self.wszystkie_tel_na_stronie_glownej = wszystkie_tel_na_stronie_glownej
        self.adres_mail = adres_mail
        self.adres_mail2 = adres_mail2
        self.adres_mail3 = adres_mail3
        self.wszystkie_adresy_mail = wszystkie_adresy_mail
        self.strona_domowa = strona_domowa
        self.dzien_urodzin = dzien_urodzin
        self.miesiac_urodzin = miesiac_urodzin
        self.rok_urodzenia = rok_urodzenia
        self.alrternatywny_adres = alrternatywny_adres
        self.tel_domowy2 = tel_domowy2
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.imie, self.nazwisko)

    def __eq__(self, other):
        return (
                       self.id is None or other.id is None or self.id == other.id) and self.nazwisko == other.nazwisko and self.imie == other.imie

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
