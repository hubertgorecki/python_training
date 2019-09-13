# -*- coding: utf-8 -*-

import pytest
from model.contact import Contact
from fixture.application_contact import ApplicationContact


@pytest.fixture
def app(request):
    fixture = ApplicationContact()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.zalogowanie(login="admin", haslo="secret")
    app.wypelnij_dane_kontaktowe_i_zapisz(Contact(imie="Janek", nazwisko="Nowak", inicjaly="JN", zwrot="Pani Magister", ulica="tajny 13", tel_domowy="12 254 87 45", tel_komorkowy="123 456 789", adres_mail="ewa.kowalska@wp.eu"))
    app.wylogowanie()
