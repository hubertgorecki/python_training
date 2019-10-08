# # -*- coding: utf-8 -*-
# from model.group import Group
#
#
# def test_edit_first_group(app):
#     # app.session.zalogowanie(login="admin", haslo="secret")
#         if app.group.licznik_checkboxow_grupy() == 0:
#         app.group.utworzenie_nowej_grupy(Group(nazwa="testowagrupa", stopka="testowastopka"))
#     stara_lista_grup = app.group.zwroc_liste_grup()
#     app.group.edycja_pierwszej_grupy(Group(nazwa="nazwa", naglowek="nagłówek", stopka="stopka"))
#     nowa_lista_grup = app.group.zwroc_liste_grup()
#     assert len(stara_lista_grup)  == len(nowa_lista_grup)
#     # app.session.wylogowanie()
