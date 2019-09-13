# -*- coding: utf-8 -*-

import pytest
from model.group import Group
# from fixture.application_group import ApplicationGroup
from fixture.menager import Menager


@pytest.fixture()
def app(request):
    fixture = Menager()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group2(app):
    app.session.zalogowanie(login="admin", haslo="secret")
    app.group.utworzenie_nowej_grupy(Group(nazwa="nowa2", naglowek="nowa2", stopka="nowa2nowa2"))
    app.session.wylogowanie()


def test_add_group3(app):
    app.session.zalogowanie(login="admin", haslo="secret")
    app.group.utworzenie_nowej_grupy(Group(nazwa="nowa grupa", naglowek="coscos", stopka="malecos"))
    app.session.wylogowanie()
