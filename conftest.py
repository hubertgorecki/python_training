# -*- coding: utf-8 -*-

import pytest
from fixture.menager import Menager


# scope = "session"  - jedno uruchomienie przegladarki i następnie uruchomienie testów.
# Bez tego - każdy test = otwarcie przegladarki co wydłuża czas.
# @pytest.fixture(scope = "session") - nie działa
@pytest.fixture
# Fixtura dla wszystkich testów. Dzięki temu nie musimy umieszczać oddzielnej fixtury w każdym tescie./
def app(request):
    fixture = Menager()
    request.addfinalizer(fixture.destroy)
    return fixture
