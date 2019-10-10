# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_edit_some_contact(app):
    # app.session.zalogowanie(login="admin", haslo="secret")
    if app.contact.licznik_checkboxow_kontakty() == 0:
        app.contact.wypelnij_dane_kontaktowe_i_zapisz(
            Contact(imie="Anna", imie2="Anka", nazwisko="Ankadaka", inicjaly="", firma="Japanaznajde",
                    zwrot="Jakiś",
                    adres="Jawna", tel_domowy="", tel_komorkowy="", tel_praca="",
                    adres_mail="jjjjj@pl.pl", adres_mail2="JJJJJ.pl.pl", strona_domowa="", dzien_urodzin="1",
                    miesiac_urodzin="July", rok_urodzenia="1111"))
    stara_lista_kontaktow = app.contact.zwroc_liste_kontaktow()
    kontakt = Contact(imie="Zenek", imie2="Juliusz", nazwisko="Zulianowski", inicjaly="JJJ", firma="Japanaznajde",
            zwrot="Jakiś", adres="Jawna", tel_domowy="", tel_komorkowy="234 432 123", tel_praca="",
            adres_mail="jjjjj@pl.pl", adres_mail2="JJJJJ.pl.pl", dzien_urodzin="1",
            miesiac_urodzin="July", rok_urodzenia="1111", alrternatywny_adres="")
    index = randrange(len(stara_lista_kontaktow))
    kontakt.id = stara_lista_kontaktow[index].id
    app.contact.edycja_losowego_kontaktu(kontakt, index)
    nowa_lista_kontaktow = app.contact.zwroc_liste_kontaktow()
    # porównanie liczby kontaktów odejmując jeden od pierwotnej liczby, w ten sposób sprawdzimy czy usunięcie się powiodło.
    assert len(stara_lista_kontaktow) == len(nowa_lista_kontaktow)
    stara_lista_kontaktow[index] = kontakt
    assert sorted(stara_lista_kontaktow, key=Contact.id_or_max) == sorted(nowa_lista_kontaktow, key=Contact.id_or_max)


def test_edit_first_contact(app):
    if app.contact.licznik_checkboxow_kontakty() == 0:
        app.contact.wypelnij_dane_kontaktowe_i_zapisz(
            Contact(imie="Anna", imie2="Anka", nazwisko="Ankadaka", inicjaly="", firma="Japanaznajde",
                    zwrot="Jakiś",
                    adres="Jawna", tel_domowy="4543255", tel_komorkowy="354353", tel_praca="4233421",
                    adres_mail="jjjjj@pl.pl", adres_mail2="JJJJJ.pl.pl", strona_domowa="", dzien_urodzin="1",
                    miesiac_urodzin="July", rok_urodzenia="1111"))
    stara_lista_kontaktow = app.contact.zwroc_liste_kontaktow()
    kontakt = Contact(imie="Zenek", imie2="Juliusz", nazwisko="Zulianowski", inicjaly="JJJ", firma="Japanaznajde",
            zwrot="Jakiś", adres="Jawna", tel_domowy="12342134", tel_komorkowy="234 432 123", tel_praca="2425415",
            adres_mail="jjjjj@pl.pl", adres_mail2="JJJJJ.pl.pl", dzien_urodzin="1",
            miesiac_urodzin="July", rok_urodzenia="1111", alrternatywny_adres="")
    kontakt.id = stara_lista_kontaktow[0].id
    app.contact.edycja_pierwszego_kontaktu(kontakt)
    nowa_lista_kontaktow = app.contact.zwroc_liste_kontaktow()
    # porównanie liczby kontaktów odejmując jeden od pierwotnej liczby, w ten sposób sprawdzimy czy usunięcie się powiodło.
    assert len(stara_lista_kontaktow) == len(nowa_lista_kontaktow)
    stara_lista_kontaktow[0] = kontakt
    assert sorted(stara_lista_kontaktow, key=Contact.id_or_max) == sorted(nowa_lista_kontaktow, key=Contact.id_or_max)
    # app.session.wylogowanie()
