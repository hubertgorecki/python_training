# -*- coding: utf-8 -*-


def test_del_first_contact(app):
    app.session.zalogowanie(login="admin", haslo="secret")
    app.contact.usuniecie_pierwszego_kontaktu()
    app.session.wylogowanie()