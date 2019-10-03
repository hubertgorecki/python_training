# -*- coding: utf-8 -*-

from model.contact import Contact

def test_add_contact(app):
    # app.session.zalogowanie(login="admin", haslo="secret")
    stara_lista_kontaktow = app.contact.zwroc_liste_kontaktow()
    kontakt = Contact(imie="A", nazwisko="BBBBBBBBBB", dzien_urodzin="12")
    app.contact.wypelnij_dane_kontaktowe_i_zapisz(kontakt)
    nowa_lista_kontaktow = app.contact.zwroc_liste_kontaktow()
    assert len(stara_lista_kontaktow) + 1 == len(nowa_lista_kontaktow)
    stara_lista_kontaktow.append(kontakt)
    # weryfikacja czy kontakt posiada identyfikator - id, jeśli nie ma zwracana jest maksymalna liczba. Specjalna maksymalna liczba - maxsize.
    assert sorted(stara_lista_kontaktow, key=Contact.id_or_max) == sorted(nowa_lista_kontaktow, key=Contact.id_or_max)
    # app.session.wylogowanie()
