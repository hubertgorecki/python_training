# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from group import Group


class TestAddGroup2(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_group2(self):
        wd = self.wd
        self.otwarcie_strony_glownej(wd)
        self.zalogowanie(wd, login="admin", haslo="secret")
        self.otwiera_strone_z_grupami(wd)
        self.utworzenie_nowej_grupy(wd, Group(nazwa="nowa2", naglowek="nowa2", stopka="nowa2nowa2"))
        self.powrot_na_strone_z_lista_grup(wd)
        self.wylogowanie(wd)

    def test_add_group3(self):
        wd = self.wd
        self.otwarcie_strony_glownej(wd)
        self.zalogowanie(wd, login="admin", haslo="secret")
        self.otwiera_strone_z_grupami(wd)
        self.utworzenie_nowej_grupy(wd, Group(nazwa="nowa grupa", naglowek="coscos", stopka="malecos"))
        self.powrot_na_strone_z_lista_grup(wd)
        self.wylogowanie(wd)

    def wylogowanie(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def powrot_na_strone_z_lista_grup(self, wd):
        wd.find_element_by_link_text("groups").click()

    def utworzenie_nowej_grupy(self, wd, Group):
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

    def otwiera_strone_z_grupami(self, wd):
        wd.find_element_by_link_text("groups").click()

    def zalogowanie(self, wd, login, haslo):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(login)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(haslo)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def otwarcie_strony_glownej(self, wd):
        wd.get("http://localhost/addressbook/group.php")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
        
    def tearDown(self):
        self.wd.quit()
 
 
if __name__ == "__main__":
    unittest.main()
