# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    stara_lista_grup = db.get_group_list()
    # group = Group(nazwa="aslkdkgajhsdlf", naglowek="adsgasgdsajfa", stopka="ROPIHa")
    app.group.utworzenie_nowej_grupy(group)
    # porównanie ilości list
    #assert len(stara_lista_grup) + 1 == len(db.get_group_list())
    # porównanie elementów listy
    nowa_lista_grup = db.get_group_list()
    stara_lista_grup.append(group)
    assert sorted(stara_lista_grup, key=Group.id_or_max) == sorted(nowa_lista_grup, key=Group.id_or_max)
    if check_ui:
            assert sorted(nowa_lista_grup, key=Group.id_or_max) == sorted(app.group.zwroc_liste_grup(), key=Group.id_or_max)

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
