from selenium import webdriver
from fixture.session import Sesja

class ApplicationGroup:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = Sesja(self)

    def powrot_na_strone_z_lista_grup(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def utworzenie_nowej_grupy(self, Group):
        wd = self.wd
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

    def otwiera_strone_z_grupami(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def otwarcie_strony_glownej(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/group.php")

    def destroy(self):
        self.wd.quit()