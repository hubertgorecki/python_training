# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_del_some_contact(app, db, check_ui):
    # app.session.zalogowanie(login="admin", haslo="secret")
    if len(db.get_contact_list()) == 0:
        app.contact.wypelnij_dane_kontaktowe_i_zapisz(
            Contact(imie="Anna", imie2="Anka", nazwisko="Ankadaka", inicjaly="", firma="Japanaznajde",
                    zwrot="Jakiś",
                    adres="Jawna", tel_domowy="", tel_komorkowy="", tel_praca="",
                    adres_mail="jjjjj@pl.pl", adres_mail2="JJJJJ.pl.pl", strona_domowa="", dzien_urodzin="1",
                    miesiac_urodzin="July", rok_urodzenia="1111", alrternatywny_adres=""))
    # przypisanie listy kontaktów przed usunięciem pierwszego z nich
    stara_lista_kontaktow = db.get_contact_list()
    losowy_kontakt = random.choice(stara_lista_kontaktow)
    app.contact.usuniecie_losowego_kontaktu_id(losowy_kontakt.id)
    # przypisanie listy kontaktów po usunięciu pierwszego
    nowa_lista_kontaktow = db.get_contact_list()
    # porównanie liczby kontaktów odejmując jeden od pierwotnej liczby, w ten sposób sprawdzimy czy usunięcie się powiodło.
    assert len(stara_lista_kontaktow) - 1 == len(nowa_lista_kontaktow)
    if check_ui:
        assert len(stara_lista_kontaktow) - 1 == len(app.contact.zwroc_liste_kontaktow())


def test_del_first_contact(app, db, check_ui):
    # app.session.zalogowanie(login="admin", haslo="secret")
    if len(db.get_contact_list()) == 0:
        app.contact.wypelnij_dane_kontaktowe_i_zapisz(
            Contact(imie="Anna", imie2="Anka", nazwisko="Ankadaka", inicjaly="", firma="Japanaznajde",
                    zwrot="Jakiś",
                    adres="Jawna", tel_domowy="", tel_komorkowy="", tel_praca="",
                    adres_mail="jjjjj@pl.pl", adres_mail2="JJJJJ.pl.pl", strona_domowa="", dzien_urodzin="1",
                    miesiac_urodzin="July", rok_urodzenia="1111", alrternatywny_adres=""))
    # przypisanie listy kontaktów przed usunięciem pierwszego z nich
    stara_lista_kontaktow = db.get_contact_list()
    app.contact.usuniecie_pierwszego_kontaktu()
    # przypisanie listy kontaktów po usunięciu pierwszego
    nowa_lista_kontaktow = db.get_contact_list()
    # porównanie liczby kontaktów odejmując jeden od pierwotnej liczby, w ten sposób sprawdzimy czy usunięcie się powiodło.
    assert len(stara_lista_kontaktow) - 1 == len(nowa_lista_kontaktow)
    if check_ui:
        assert len(stara_lista_kontaktow) - 1 == len(app.contact.zwroc_liste_kontaktow())