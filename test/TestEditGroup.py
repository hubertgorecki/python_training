# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group(app):
    app.session.zalogowanie(login="admin", haslo="secret")
    app.group.edycja_pierwszej_grupy(Group(nazwa="nazwa", naglowek="nagłówek", stopka="stopka"))
    app.session.wylogowanie()
