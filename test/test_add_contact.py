# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact


# przekazanie danych testowych w charakterze parametru. Przekazujemy do parametru "contact" dane z dane_testowe
# @pytest.mark.parametrize("kontakt", dane_testowe_kontakt, ids=[repr(x) for x in dane_testowe_kontakt])
def test_add_contact(app, json_contacts):
    # pass
    stara_lista_kontaktow = app.contact.zwroc_liste_kontaktow()
    app.contact.wypelnij_dane_kontaktowe_i_zapisz(json_contacts)
    nowa_lista_kontaktow = app.contact.zwroc_liste_kontaktow()
    assert len(stara_lista_kontaktow) + 1 == len(nowa_lista_kontaktow)
    stara_lista_kontaktow.append(json_contacts)
    # weryfikacja czy kontakt posiada identyfikator - id, jeśli nie ma zwracana jest maksymalna liczba. Specjalna maksymalna liczba - maxsize.
    assert sorted(stara_lista_kontaktow, key=Contact.id_or_max) == sorted(nowa_lista_kontaktow, key=Contact.id_or_max)
