# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_edit_group_name(app, db, check_ui):
    # app.session.zalogowanie(login="admin", haslo="secret")
    if app.group.licznik_checkboxow_grupy() == 0:
        app.group.utworzenie_nowej_grupy(Group(nazwa="testowagrupa", stopka="testowastopka"))
    stara_lista_grup = db.get_group_list()
    group = Group(nazwa="Nowa nazwa grupy")
    losowa_grupa = random.choice(stara_lista_grup)
    # group.id = stara_lista_grup[index].id
    app.group.edycja_grupy_z_id(losowa_grupa.id, group)
    # porównanie listy grup
    nowa_lista_grup = db.get_group_list()
    assert len(stara_lista_grup) == len(nowa_lista_grup)
    # porównanie id i nazw
    if check_ui:
        assert sorted(stara_lista_grup, key=Group.id_or_max) == sorted(app.group.zwroc_liste_grup(),
                                                                       key=Group.id_or_max)

# def test_edit_group_header(app):
#     # app.session.zalogowanie(login="admin", haslo="secret")
#     stara_lista_grup = app.group.zwroc_liste_grup()
#     if app.group.licznik_checkboxow_grupy() == 0:
#         app.group.utworzenie_nowej_grupy(Group(nazwa="testowagrupa", stopka="testowastopka"))
#     app.group.edycja_pierwszej_grupy(Group(naglowek="sagbasfgasgvatgcafceW"))
#     nowa_lista_grup = app.group.zwroc_liste_grup()
#     assert len(stara_lista_grup)  == len(nowa_lista_grup)
#     # app.session.wylogowanie()
