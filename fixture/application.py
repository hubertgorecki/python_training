# -*- coding: utf-8 -*-

from selenium import webdriver
from fixture.session import Sesja
from fixture.group import Grupy
from fixture.contact import Kontakty


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        # self.wd.implicitly_wait(3)
        self.session = Sesja(self)
        self.group = Grupy(self)
        self.contact = Kontakty(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def otwarcie_strony_glownej(self):
        wd = self.wd
        if wd.current_url.endswith("http://localhost/addressbook/") and len(wd.find_elements_by_name("add")) > 0:
            return
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
