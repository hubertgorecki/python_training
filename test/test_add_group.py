# -*- coding: utf-8 -*-

from model.group import Group
import pytest
import random
import string

# zwraca losowo generowane łańcuchy
def zwroc_ciag_znakow(prefix, maxlen):
    ciag_znakow = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(ciag_znakow) for i in range(random.randrange(maxlen))])


# zwraca losowe ciągi znaków dla nazwy, naglówków, stopek (5 razy pierwszą grupę generuje) + puste.
dane_testowe_grupy = [Group(nazwa="", naglowek="", stopka="")] + [
    Group(nazwa=zwroc_ciag_znakow("nazwa", 10), naglowek=zwroc_ciag_znakow("naglowek", 20),
          stopka=zwroc_ciag_znakow("stopka", 10)) for i in range(5)
]


# zwraca losowe ciągi znaków dla nazwy, naglówków, stopek - ich kombinacje.
# dane_testowe = [Group(nazwa=nazwa, naglowek=naglowek, stopka=stopka)
#                 for nazwa in [" ", zwroc_ciag_znakow("nazwa",10)]
#                 for naglowek in [" ", zwroc_ciag_znakow("naglowek", 10)]
#                 for stopka in [" ", zwroc_ciag_znakow("stopka", 10)]]

# przekazanie danych testowych w charakterze parametru. Przekazujemy do parametru "group" dane z dane_testowe

@pytest.mark.parametrize("group", dane_testowe_grupy, ids=[repr(x) for x in dane_testowe_grupy])
def test_add_group(app, group):
    # pass
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
