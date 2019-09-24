# -*- coding: utf-8 -*-

def test_del_first_group(app):
    # app.session.zalogowanie(login="admin", haslo="secret")
    app.group.usuniecie_pierwszej_grupy()
    # app.session.wylogowanie()
