# -*- coding: utf-8 -*-

from model.group import Group

class Grupy:
    def __init__(self, app):
        self.app = app

    # def powrot_na_strone_z_lista_grup(self):
    #     wd = self.app.wd
    #     wd.find_element_by_link_text("groups").click()

    def otwiera_strone_z_grupami(self):
        wd = self.app.wd
        if wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0:
            return
        wd.find_element_by_link_text("groups").click()

    def utworzenie_nowej_grupy(self, group):
        wd = self.app.wd
        self.otwiera_strone_z_grupami()
        # Rozpoczynamy tworzenie nowej grupy
        wd.find_element_by_name("new").click()
        self.wypelnienie_formularza_danymi_grupy(group)
        # Submit - Tworzymy nową grupę
        wd.find_element_by_name("submit").click()
        self.otwiera_strone_z_grupami()
        self.group_cache = None

    def wypelnienie_formularza_danymi_grupy(self, group):
        wd = self.app.wd
        # Wypełniamy formularz danymi
        self.zmien_tresc_danego_pola("group_name", group.nazwa)
        self.zmien_tresc_danego_pola("group_header", group.naglowek)
        self.zmien_tresc_danego_pola("group_footer", group.stopka)

    def zmien_tresc_danego_pola(self, nazwa_pola, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(nazwa_pola).click()
            wd.find_element_by_name(nazwa_pola).clear()
            wd.find_element_by_name(nazwa_pola).send_keys(text)

    def usuniecie_pierwszej_grupy(self):
        self.usuniecie_grupy_z_indexem(0)

    def usuniecie_grupy_z_indexem(self, index):
        wd = self.app.wd
        self.otwiera_strone_z_grupami()
        self.wyszukaj_grupe_z_indexem(index)
        # szukamy przycisku usuń i klikamy
        wd.find_element_by_name("delete").click()
        self.group_cache = None

    def usuniecie_grupy_z_id(self, id):
        wd = self.app.wd
        self.otwiera_strone_z_grupami()
        self.wyszukaj_grupe_z_id(id)
        # szukamy przycisku usuń i klikamy
        wd.find_element_by_name("delete").click()
        self.group_cache = None

    def wyszukaj_pierwsza_grupe(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def wyszukaj_grupe_z_indexem(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def wyszukaj_grupe_z_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def edycja_pierwszej_grupy(self):
        self.edycja_grupy_z_indexem(0)

    def edycja_grupy_z_indexem(self, group, index):
        wd = self.app.wd
        self.otwiera_strone_z_grupami()
        self.wyszukaj_grupe_z_indexem(index)
        # otwarcie edycji grupy
        wd.find_element_by_name("edit").click()
        self.wypelnienie_formularza_danymi_grupy(group)
        wd.find_element_by_name("update").click()
        self.otwiera_strone_z_grupami()
        self.group_cache = None

    def edycja_grupy_z_id(self, id, group):
        wd = self.app.wd
        self.otwiera_strone_z_grupami()
        self.wyszukaj_grupe_z_id(id)
        # otwarcie edycji grupy
        wd.find_element_by_name("edit").click()
        self.wypelnienie_formularza_danymi_grupy(group)
        wd.find_element_by_name("update").click()
        self.otwiera_strone_z_grupami()
        self.group_cache = None

    def licznik_checkboxow_grupy(self):
        wd = self.app.wd
        self.otwiera_strone_z_grupami()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def zwroc_liste_grup(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.otwiera_strone_z_grupami()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(nazwa=text, id=id))
        return list(self.group_cache)


