# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    app.session.zalogowanie(login="admin", haslo="secret")
    app.contact.wypelnij_dane_kontaktowe_i_zapisz(
        Contact(imie="Janek", nazwisko="Nowak", inicjaly="JN", zwrot="Pani Magister", ulica="tajny 13",
                tel_domowy="12 254 87 45", tel_komorkowy="123 456 789", adres_mail="ewa.kowalska@wp.eu"))
    app.session.wylogowanie()
