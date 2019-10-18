# -*- coding: utf-8 -*-
from model.group import Group
import pytest
# from data.groups import losowe_dane_testowe_grupy


# przekazanie danych testowych w charakterze parametru. Przekazujemy do parametru "group" dane z dane_testowe
# @pytest.mark.parametrize("group", losowe_dane_testowe_grupy, ids=[repr(x) for x in losowe_dane_testowe_grupy])
def test_add_group(app, json_groups):
    group = json_groups
    stara_lista_grup = app.group.zwroc_liste_grup()
    # group = Group(nazwa="aslkdkgajhsdlf", naglowek="adsgasgdsajfa", stopka="ROPIHa")
    app.group.utworzenie_nowej_grupy(group)
    # porównanie ilości list
    assert len(stara_lista_grup) + 1 == app.group.licznik_checkboxow_grupy()
    # porównanie elementów listy
    nowa_lista_grup = app.group.zwroc_liste_grup()
    stara_lista_grup.append(group)
    assert sorted(stara_lista_grup, key=Group.id_or_max) == sorted(nowa_lista_grup, key=Group.id_or_max)

# def test_add_group2(app):
#     stara_lista_grup = app.group.zwroc_liste_grup()
#     group = Group(nazwa="", naglowek="", stopka="")
#     app.group.utworzenie_nowej_grupy(group)
#     #porównanie ilości list
#     nowa_lista_grup = app.group.zwroc_liste_grup()
#     assert len(stara_lista_grup)+1 == len(nowa_lista_grup)
#     #porównanie elementów listy
#     stara_lista_grup.append(group)
#     assert sorted(stara_lista_grup, key=Group.id_or_max) == sorted(nowa_lista_grup, key=Group.id_or_max)
