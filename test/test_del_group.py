# -*- coding: utf-8 -*-
from model.group import Group


def test_del_first_group(app):
    # app.session.zalogowanie(login="admin", haslo="secret")
    stara_lista_grup = app.group.zwroc_liste_grup()
    if app.group.licznik_checkboxow_grupy() == 0:
        app.group.utworzenie_nowej_grupy(Group(nazwa="Specjalna"))
    app.group.usuniecie_pierwszej_grupy()
    nowa_lista_grup = app.group.zwroc_liste_grup()
    assert len(stara_lista_grup) - 1 == len(nowa_lista_grup)
    #usunięcie pierwszej listy i porównanie
    stara_lista_grup[0:1] = []
    assert stara_lista_grup == nowa_lista_grup
    # app.session.wylogowanie()
