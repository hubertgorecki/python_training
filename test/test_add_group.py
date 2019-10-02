# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    # app.session.zalogowanie(login="admin", haslo="secret")
    stara_lista_grup = app.group.zwroc_liste_grup()
    group = Group(nazwa="aslkdkgajhsdlf", naglowek="adsgasgdsajfa", stopka="ROPIHa")
    app.group.utworzenie_nowej_grupy(group)
    # porównanie ilości list
    nowa_lista_grup = app.group.zwroc_liste_grup()
    assert len(stara_lista_grup)+1 == len(nowa_lista_grup)
    # porównanie elementów listy
    stara_lista_grup.append(group)
    assert sorted(stara_lista_grup, key=Group.id_or_max) == sorted(nowa_lista_grup, key=Group.id_or_max)
    # app.session.wylogowanie()


def test_add_group2(app):
    # app.session.zalogowanie(login="admin", haslo="secret")
    stara_lista_grup = app.group.zwroc_liste_grup()
    group = Group(nazwa="nowa grupa", naglowek="coscos", stopka="malecos")
    app.group.utworzenie_nowej_grupy(group)
    #porównanie ilości list
    nowa_lista_grup = app.group.zwroc_liste_grup()
    assert len(stara_lista_grup)+1 == len(nowa_lista_grup)
    #porównanie elementów listy
    stara_lista_grup.append(group)
    assert sorted(stara_lista_grup, key=Group.id_or_max) == sorted(nowa_lista_grup, key=Group.id_or_max)

    # app.session.wylogowanie()
