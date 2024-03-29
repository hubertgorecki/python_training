# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
from test.test_add_contact_to_group import test_add_contact_to_group
import random


def test_del_contact_in_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.wypelnij_dane_kontaktowe_i_zapisz(
            Contact(imie="Anna", imie2="Anka", nazwisko="Ankadaka", inicjaly="", firma="Japanaznajde",
                    zwrot="Jakiś",
                    adres="Jawna", tel_domowy="", tel_komorkowy="", tel_praca="",
                    adres_mail="jjjjj@pl.pl", adres_mail2="JJJJJ.pl.pl", strona_domowa="", dzien_urodzin="1",
                    miesiac_urodzin="July", rok_urodzenia="1111"))
    if app.group.licznik_checkboxow_grupy() == 0:
        app.group.utworzenie_nowej_grupy(Group(nazwa="testowagrupa", stopka="testowastopka"))
    if len(db.get_contact_in_groups_list()) == 0:
        test_add_contact_to_group(app, db)
    stara_lista_kontaktow_w_grupie = db.get_contact_in_groups_list()
    losowy_kontakt_grupy_kontaktow = random.choice(stara_lista_kontaktow_w_grupie)
    app.contact.usun_losowy_kontakt_id_z_losowej_grupy(losowy_kontakt_grupy_kontaktow.id,
                                                       losowy_kontakt_grupy_kontaktow.group_id)
    nowa_lista_kontaktow_w_grupie = db.get_contact_in_groups_list()
    assert len(stara_lista_kontaktow_w_grupie) - 1 == len(nowa_lista_kontaktow_w_grupie)
