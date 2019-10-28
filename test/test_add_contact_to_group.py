# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.wypelnij_dane_kontaktowe_i_zapisz(
            Contact(imie="Anna", imie2="Anka", nazwisko="Ankadaka", inicjaly="", firma="Japanaznajde",
                    zwrot="Jakiś",
                    adres="Jawna", tel_domowy="", tel_komorkowy="", tel_praca="",
                    adres_mail="jjjjj@pl.pl", adres_mail2="JJJJJ.pl.pl", strona_domowa="", dzien_urodzin="1",
                    miesiac_urodzin="July", rok_urodzenia="1111"))
    if app.group.licznik_checkboxow_grupy() == 0:
        app.group.utworzenie_nowej_grupy(Group(nazwa="testowagrupa", stopka="testowastopka"))
    lista_kontaktow = db.get_contact_list()
    losowy_kontakt = random.choice(lista_kontaktow)
    lista_grup = db.get_group_list()
    losowa_grupa = random.choice(lista_grup)
    stara_lista_kontaktow_w_grupie = db.get_contact_in_groups_list()
    app.contact.dodaj_losowy_kontakt_id_do_losowej_grupy(losowy_kontakt.id, losowa_grupa.nazwa)
    nowa_lista_kontaktow_w_grupie = db.get_contact_in_groups_list()
    assert len(stara_lista_kontaktow_w_grupie) + 1 == len(nowa_lista_kontaktow_w_grupie)
