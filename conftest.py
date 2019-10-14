# -*- coding: utf-8 -*-

import pytest
from fixture.application import Application

# scope = "session"  - jedno uruchomienie przegladarki i następnie uruchomienie testów.
# Bez tego - każdy test = otwarcie przegladarki co wydłuża czas.
# @pytest.fixture(scope = "session")

fixture = None


@pytest.fixture
# Fixtura dla wszystkich testów. Dzięki temu nie musimy umieszczać oddzielnej fixtury w każdym tescie./
def app(request):
    global fixture
    # możliwość wyboru przeglarkiw  której uruchamia się testy, wpisania hasła i loginu oraz adresu bezpośrednio z konsoli
    login = request.config.getoption("--login")
    haslo = request.config.getoption("--haslo")
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--baseUrl")
    if fixture is None:
        fixture = Application(browser=browser, base_url=base_url)
    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.session.czy_trzeba_sie_zalogowac(login=login, haslo=haslo)
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.czy_trzeba_sie_wylogowac()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="Chrome")
    parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/")
    parser.addoption("--login", action="store", default="admin")
    parser.addoption("--haslo", action="store", default="secret")
