

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