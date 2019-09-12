# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from contact import Contact


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        self.otworz_strone_glowna(wd)
        self.zalogowanie(wd,login="admin", haslo="secret")
        self.otworz_strone_z_kontaktami(wd)
        self.wypelnij_dane_kontaktowe_i_zapisz(wd, Contact(imie="Janek", nazwisko="Nowak", inicjaly="JN", zwrot="Pani Magister", ulica="tajny 13", tel_domowy="12 254 87 45", tel_komorkowy="123 456 789", adres_mail="ewa.kowalska@wp.eu"))
        self.wyswietl_strone_glowna(wd)

    def wyswietl_strone_glowna(self, wd):
        wd.find_element_by_link_text("home").click()

    def wypelnij_dane_kontaktowe_i_zapisz(self, wd, contact):
        # wypełnienie danych kontaktowych
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.imie)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.nazwisko)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.inicjaly)
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.zwrot)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.ulica)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.tel_domowy)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.tel_komorkowy)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.adres_mail)
        # zapisanie danych kontaktowych
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def otworz_strone_z_kontaktami(self, wd):
        wd.find_element_by_link_text("add new").click()

    def zalogowanie(self, wd, login, haslo):
        # logowanie (uzupełnia dane i loguje)
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(login)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(haslo)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def otworz_strone_glowna(self, wd):
        wd.get("http://localhost/addressbook/")

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
