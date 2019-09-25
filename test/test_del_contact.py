# -*- coding: utf-8 -*-
from model.contact import Contact

def test_del_first_contact(app):
    # app.session.zalogowanie(login="admin", haslo="secret")
    if app.contact.licznik_checkboxow_kontakty() == 0:
        app.contact.wypelnij_dane_kontaktowe_i_zapisz(
            Contact(imie="Anna", imie2="Anka", nazwisko="Ankadaka", inicjaly="", firma="Japanaznajde",
                    zwrot="Jakiś",
                    adres="Jawna", tel_domowy="", tel_komorkowy="", tel_praca="",
                    adres_mail="jjjjj@pl.pl", adres_mail2="JJJJJ.pl.pl", strona_domowa="", dzien_urodzin="1",
                    miesiac_urodzin="July", rok_urodzenia="1111", alrternatywny_adres=""))
    app.contact.usuniecie_pierwszego_kontaktu()
    # app.session.wylogowanie()
