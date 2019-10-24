# -*- coding: utf-8 -*-
from model.contact import Contact


# przekazanie danych testowych w charakterze parametru. Przekazujemy do parametru "contact" dane z dane_testowe
# @pytest.mark.parametrize("kontakt", dane_testowe_kontakt, ids=[repr(x) for x in dane_testowe_kontakt])
def test_add_contact(app, db, json_contacts, check_ui):
    # pass
    stara_lista_kontaktow = db.get_contact_list()
    app.contact.wypelnij_dane_kontaktowe_i_zapisz(json_contacts)
    nowa_lista_kontaktow = db.get_contact_list()
    # dodaje do starej listy kontaktow to co zostalo dodane z pliku json_contact
    stara_lista_kontaktow.append(json_contacts)
    assert len(stara_lista_kontaktow) == len(nowa_lista_kontaktow)
    # weryfikacja czy kontakt posiada identyfikator - id, jeśli nie ma zwracana jest maksymalna liczba. Specjalna maksymalna liczba - maxsize.
    # assert sorted(stara_lista_kontaktow, key=Contact.id_or_max) == sorted(nowa_lista_kontaktow, key=Contact.id_or_max)
    if check_ui:
        assert len(stara_lista_kontaktow) == len(app.contact.zwroc_liste_kontaktow())
