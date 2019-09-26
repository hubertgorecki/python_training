# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    # app.session.zalogowanie(login="admin", haslo="secret")
    app.contact.wypelnij_dane_kontaktowe_i_zapisz(
        Contact(imie="A", dzien_urodzin="12"))
    # app.session.wylogowanie()
