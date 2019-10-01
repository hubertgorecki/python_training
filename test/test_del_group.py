# -*- coding: utf-8 -*-
from model.group import Group


def test_del_first_group(app):
    # app.session.zalogowanie(login="admin", haslo="secret")
    if app.group.licznik_checkboxow_grupy() == 0:
        app.group.utworzenie_nowej_grupy(Group(nazwa="Specjalna"))
    app.group.usuniecie_pierwszej_grupy()
    # app.session.wylogowanie()
