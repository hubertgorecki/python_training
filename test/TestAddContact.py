# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    app.session.zalogowanie(login="admin", haslo="secret")
    app.contact.wypelnij_dane_kontaktowe_i_zapisz(
        Contact(imie="Alfred", imie2="Jonatan", nazwisko="Baran", inicjaly="AJB", firma="Google", zwrot="Prezes",
                adres="Ukryta", tel_domowy="112 12 32", tel_komorkowy="234 432 123", tel_praca="098 765 432",
                adres_mail="lkjh@pl.pl", adres_mail2="wsda.pl.pl", strona_domowa="auto.pl", dzien_urodzin="14",
                miesiac_urodzin="9", rok_urodzenia="1982", alrternatywny_adres="brak"))
    app.session.wylogowanie()
