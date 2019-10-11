# -*- coding: utf-8 -*-
import pytest
import random
import string
import datetime
from model.contact import Contact

nazwy_miesiecy = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                  "November",
                  "December"]


def zwroc_ciag_znakow(prefix, maxlen):
    ciag_znakow = string.ascii_letters + string.digits + " " * 4
    return prefix + "".join([random.choice(ciag_znakow) for i in range(random.randrange(maxlen))])


def zwroc_numer_tel(prefix, maxlen):
    numer_telefonu = string.digits
    return prefix + "+ " + "".join([random.choice(numer_telefonu) for i in range(random.randrange(maxlen))])


def zwroc_email(prefix, maxlen):
    adres_mail = string.ascii_lowercase + string.digits
    domena = "".join([random.choice(string.ascii_lowercase) for i in range(random.randrange(5))])
    return prefix + "".join([random.choice(adres_mail) for i in range(random.randrange(maxlen))]) + "@" + domena + ".pl"


def zwroc_adres_www(prefix, maxlen):
    adres_strony_www = string.ascii_lowercase
    losowy = "".join([random.choice(adres_strony_www) for i in range(random.randrange(maxlen))])
    return prefix + "www." + losowy + ".pl"


def zwroc_dzien_urodzin():
    dzien = random.randint(1, 31)
    return str(dzien)


def zwroc_miesiac_urodzin():
    miesiac = random.choice(nazwy_miesiecy)
    return miesiac


def zwroc_rok_urodzin():
    rok_biezacy = random.randint(1920, 2000)
    return str(rok_biezacy)


dane_testowe_kontakt = [
    Contact(imie=zwroc_ciag_znakow("imie: ", 8), imie2=zwroc_ciag_znakow("imie2: ", 8),
            nazwisko=zwroc_ciag_znakow("nazwisko: ", 10),
            inicjaly=zwroc_ciag_znakow("inicjały: ", 2),
            firma=zwroc_ciag_znakow("firma: ", 6), zwrot=zwroc_ciag_znakow("zwrot: ", 2),
            adres=zwroc_ciag_znakow("adres: ", 10),
            tel_domowy=zwroc_numer_tel("Tel_dom: ", 9),
            tel_komorkowy=zwroc_numer_tel("Tel_kom: ", 9),
            tel_praca=zwroc_numer_tel("Tel_prac: ", 9), tel_fax=zwroc_numer_tel("Tel_fax: ", 9),
            adres_mail=zwroc_email("mail: ", 10),
            adres_mail2=zwroc_email("mail2: ", 10),
            adres_mail3=zwroc_email("mail3: ", 10),
            strona_domowa=zwroc_adres_www("str_dom: ", 20),
            dzien_urodzin=zwroc_dzien_urodzin(),
            miesiac_urodzin=zwroc_miesiac_urodzin(),
            rok_urodzenia=zwroc_rok_urodzin(),
            alrternatywny_adres=zwroc_ciag_znakow("adres2: ", 10),
            tel_domowy2=zwroc_numer_tel("Tel_dom2: ", 9)
            ) for i in range(5)]


@pytest.mark.parametrize("kontakt", dane_testowe_kontakt, ids=[repr(x) for x in dane_testowe_kontakt])
def test_add_contact(app, kontakt):
    # pass
    stara_lista_kontaktow = app.contact.zwroc_liste_kontaktow()
    app.contact.wypelnij_dane_kontaktowe_i_zapisz(kontakt)
    nowa_lista_kontaktow = app.contact.zwroc_liste_kontaktow()
    assert len(stara_lista_kontaktow) + 1 == len(nowa_lista_kontaktow)
    stara_lista_kontaktow.append(kontakt)
    # weryfikacja czy kontakt posiada identyfikator - id, jeśli nie ma zwracana jest maksymalna liczba. Specjalna maksymalna liczba - maxsize.
    assert sorted(stara_lista_kontaktow, key=Contact.id_or_max) == sorted(nowa_lista_kontaktow, key=Contact.id_or_max)
