# -*- coding: utf-8 -*-

class Grupy:
    def __init__(self, app):
        self.app = app

    def powrot_na_strone_z_lista_grup(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def utworzenie_nowej_grupy(self, Group):
        wd = self.app.wd
        self.otwiera_strone_z_grupami()
        # Rozpoczynamy tworzenie nowej grupy
        wd.find_element_by_name("new").click()
        # Wypełniamy formularz danymi
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(Group.nazwa)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(Group.naglowek)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(Group.stopka)
        # Submit - Tworzymy nową grupę
        wd.find_element_by_name("submit").click()
        self.powrot_na_strone_z_lista_grup()

    def usuniecie_pierwszej_grupy(self):
        wd = self.app.wd
        self.otwiera_strone_z_grupami()
        # szukamy pierwszej grupy i zaznaczamy
        wd.find_element_by_name("selected[]").click()
        # szukamy przycisku usuń i klikamy
        wd.find_element_by_name("delete").click()

    def otwiera_strone_z_grupami(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
