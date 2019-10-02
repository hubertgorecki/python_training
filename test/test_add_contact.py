# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    # app.session.zalogowanie(login="admin", haslo="secret")
    stara_lista_kontaktow = app.contact.zwroc_liste_kontaktow()
    app.contact.wypelnij_dane_kontaktowe_i_zapisz(
        Contact(imie="A", dzien_urodzin="12"))
    nowa_lista_kontaktow = app.contact.zwroc_liste_kontaktow()
    assert len(stara_lista_kontaktow) + 1 == len(nowa_lista_kontaktow)
    # app.session.wylogowanie()
