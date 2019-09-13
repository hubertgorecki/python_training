# from selenium import webdriver
# from fixture.session import Sesja
# from fixture.contact import Kontakty
#
#
# class ApplicationContact:
#     def __init__ (self):
#         self.wd = webdriver.Firefox()
#         self.wd.implicitly_wait(30)
#         self.session = Sesja(self)
#         self.contact = Kontakty(self)
#
#     def otwarcie_strony_glownej(self):
#         wd = self.wd
#         wd.get("http://localhost/addressbook/group.php")
#
#     def destroy(self):
#         self.wd.quit()