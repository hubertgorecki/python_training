# -*- coding: utf-8 -*-

import pytest
from fixture.application import Application

# scope = "session"  - jedno uruchomienie przegladarki i następnie uruchomienie testów.
# Bez tego - każdy test = otwarcie przegladarki co wydłuża czas.
# @pytest.fixture(scope = "session")

fixture = None


@pytest.fixture
# Fixtura dla wszystkich testów. Dzięki temu nie musimy umieszczać oddzielnej fixtury w każdym tescie./
def app():
    global fixture
    if fixture is None:
        fixture = Application()
    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.session.czy_trzeba_sie_zalogowac(login="admin", haslo="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.czy_trzeba_sie_wylogowac()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture
