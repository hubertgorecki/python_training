from selenium import webdriver
from fixture.session import Sesja
from fixture.group import Grupy

class ApplicationGroup:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = Sesja(self)
        self.group = Grupy(self)

    def otwarcie_strony_glownej(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()