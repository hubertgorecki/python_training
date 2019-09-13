# -*- coding: utf-8 -*-

import pytest
from model.group import Group
from fixture.application_group import ApplicationGroup


@pytest.fixture()
def app(request):
    fixture = ApplicationGroup()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group2(app):
    app.zalogowanie(login="admin", haslo="secret")
    app.utworzenie_nowej_grupy(Group(nazwa="nowa2", naglowek="nowa2", stopka="nowa2nowa2"))
    app.wylogowanie()


def test_add_group3(app):
    app.zalogowanie(login="admin", haslo="secret")
    app.utworzenie_nowej_grupy(Group(nazwa="nowa grupa", naglowek="coscos", stopka="malecos"))
    app.wylogowanie()
