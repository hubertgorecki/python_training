# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange

# def test_del_first_group(app):
#     # app.session.zalogowanie(login="admin", haslo="secret")
#         if app.group.licznik_checkboxow_grupy() == 0:
#         app.group.utworzenie_nowej_grupy(Group(nazwa="Specjalna"))
#     stara_lista_grup = app.group.zwroc_liste_grup()
#     app.group.usuniecie_pierwszej_grupy()
#     nowa_lista_grup = app.group.zwroc_liste_grup()
#     assert len(stara_lista_grup) - 1 == len(nowa_lista_grup)
#     #usunięcie pierwszej listy i porównanie
#     stara_lista_grup[0:1] = []
#     assert stara_lista_grup == nowa_lista_grup
#     # app.session.wylogowanie()

def test_del_some_group(app):
    # app.session.zalogowanie(login="admin", haslo="secret")
    if app.group.licznik_checkboxow_grupy() == 0:
        app.group.utworzenie_nowej_grupy(Group(nazwa="Specjalna"))
    stara_lista_grup = app.group.zwroc_liste_grup()
    index = randrange(len(stara_lista_grup))
    app.group.usuniecie_grupy_z_indexem(index)
    nowa_lista_grup = app.group.zwroc_liste_grup()
    assert len(stara_lista_grup) - 1 == len(nowa_lista_grup)
    #usunięcie pierwszej listy i porównanie
    stara_lista_grup[index:index+1] = []
    assert stara_lista_grup == nowa_lista_grup
