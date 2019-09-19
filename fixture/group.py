# -*- coding: utf-8 -*-


class Grupy:
    def __init__(self, app):
        self.app = app

    def powrot_na_strone_z_lista_grup(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def utworzenie_nowej_grupy(self, group):
        wd = self.app.wd
        self.otwiera_strone_z_grupami()
        # Rozpoczynamy tworzenie nowej grupy
        wd.find_element_by_name("new").click()
        self.wypelnienie_formularza_danymi_grupy(group)
        # Submit - Tworzymy nową grupę
        wd.find_element_by_name("submit").click()
        self.powrot_na_strone_z_lista_grup()

    def wypelnienie_formularza_danymi_grupy(self, group):
        wd = self.app.wd
        # Wypełniamy formularz danymi
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.nazwa)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.naglowek)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.stopka)

    def usuniecie_pierwszej_grupy(self):
        wd = self.app.wd
        self.otwiera_strone_z_grupami()
        # szukamy pierwszej grupy i zaznaczamy
        wd.find_element_by_name("selected[]").click()
        # szukamy przycisku usuń i klikamy
        wd.find_element_by_name("delete").click()

    def edycja_pierwszej_grupy(self, group):
        wd = self.app.wd
        self.otwiera_strone_z_grupami()
        # szukamy pierwszej grupy i zaznaczamy
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        self.wypelnienie_formularza_danymi_grupy(group)
        wd.find_element_by_name("update").click()
        self.otwiera_strone_z_grupami()

    def otwiera_strone_z_grupami(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
