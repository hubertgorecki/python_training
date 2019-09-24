# -*- coding: utf-8 -*-


class Sesja:
    def __init__(self, app):
        self.app = app

    def zalogowanie(self, login, haslo):
        wd = self.app.wd
        self.app.otwarcie_strony_glownej()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(login)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(haslo)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def wylogowanie(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    def czy_trzeba_sie_wylogowac(self):
        # wd = self.app.wd
        if self.czy_zalogowany():
            self.wylogowanie()

    def czy_zalogowany(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def czy_zalogowany_jako(self, login):
        wd = self.app.wd
        return wd.find_element_by_xpath("//*[@id='top']/form/b").text == "("+login+")"

    def czy_trzeba_sie_zalogowac(self, login, haslo):
        # wd = self.app.wd
        # if self.czy_zalogowany():
        #     if self.czy_zalogowany_jako(login):
        #         return
        #     else:
        #         self.wylogowanie()
        self.zalogowanie(login, haslo)


