# -*- coding: utf-8 -*-
from model.group import Group
import random

def test_del_some_group(app, db, check_ui):
    # app.session.zalogowanie(login="admin", haslo="secret")
    if len(db.get_group_list()) == 0:
        app.group.utworzenie_nowej_grupy(Group(nazwa="Specjalna"))
    stara_lista_grup = db.get_group_list()
    losowa_grupa = random.choice(stara_lista_grup)
    app.group.usuniecie_grupy_z_id(losowa_grupa.id)
    nowa_lista_grup = db.get_group_list()
    #assert len(stara_lista_grup) - 1 == len(nowa_lista_grup)
    #usunięcie pierwszej listy i porównanie
    #stara_lista_grup.remove(losowa_grupa)
    #assert stara_lista_grup == nowa_lista_grup
    if check_ui:
            assert sorted(nowa_lista_grup, key=Group.id_or_max) == sorted(app.group.zwroc_liste_grup(), key=Group.id_or_max)