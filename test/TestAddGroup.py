# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    app.session.zalogowanie(login="admin", haslo="secret")
    app.group.utworzenie_nowej_grupy(Group(nazwa="nowa2", naglowek="nowa2", stopka="nowa2nowa2"))
    app.session.wylogowanie()


def test_add_group2(app):
    app.session.zalogowanie(login="admin", haslo="secret")
    app.group.utworzenie_nowej_grupy(Group(nazwa="nowa grupa", naglowek="coscos", stopka="malecos"))
    app.session.wylogowanie()
