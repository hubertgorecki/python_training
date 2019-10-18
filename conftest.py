# -*- coding: utf-8 -*-

import pytest
import json
import os.path
import importlib
from fixture.application import Application

# scope = "session"  - jedno uruchomienie przegladarki i następnie uruchomienie testów.
# Bez tego - każdy test = otwarcie przegladarki co wydłuża czas.
# @pytest.fixture(scope = "session")

fixture = None
target = None


@pytest.fixture
# Fixtura dla wszystkich testów. Dzięki temu nie musimy umieszczać oddzielnej fixtury w każdym tescie./
def app(request):
    # wskaczujemy żę planujemy wykorzystywać foxture i target
    global fixture
    global target
    # możliwość wyboru przeglarkiw  której uruchamia się testy, wpisania hasła i loginu oraz adresu bezpośrednio z konsoli
    browser = request.config.getoption("--browser")
    # os.path.abspath wskazuje lokalizację - absolutną, os.path.dirname wskazuje katalog w którym ten plik się znajduje, os.path.join - przykleja lokalizację pliku configuracyjnego

    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        # with - dzięki zastosowaniu tej formy nie musimy zamykać pliku. Automatycznie jest zamykany po przejściu całej metody/funkcji
        with open(config_file) as f:
            target = json.load(f)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target["baseUrl"])
    fixture.session.czy_trzeba_sie_zalogowac(login=target["login"], haslo=target["haslo"])
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
    parser.addoption("--target", action="store", default="target.json")
    # parser.addoption("--login", action="store", default="admin")
    # parser.addoption("--haslo", action="store", default="secret")

def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            stale_dane_testowe = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, stale_dane_testowe, ids=[str(x) for x in stale_dane_testowe])
        elif:
            if fixture.startswith("json_"):
                stale_dane_testowe = load_from_json(fixture[5:])
                metafunc.parametrize(fixture, stale_dane_testowe, ids=[str(x) for x in stale_dane_testowe])

def load_from_module(module):
    return importlib.import_module("data.%s" % module).stale_dane_testowe

def load_from_json(file):
    return importlib.import_module("data.%s" % module).stale_dane_testowe