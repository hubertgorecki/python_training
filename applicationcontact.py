from selenium import webdriver


class ApplicationContact:
    def __init__ (self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def wyswietl_strone_glowna(self):
        wd = self.wd
        wd.find_element_by_link_text("home").click()

    def wypelnij_dane_kontaktowe_i_zapisz(self,contact):
        wd = self.wd
        self.otworz_strone_z_kontaktami()
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
        self.wyswietl_strone_glowna()

    def otworz_strone_z_kontaktami(self):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()

    def zalogowanie(self, login, haslo):
        wd = self.wd
        self.otworz_strone_glowna()
        # logowanie (uzupełnia dane i loguje)
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(login)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(haslo)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def otworz_strone_glowna(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def wylogowanie(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def destroy(self):
        self.wd.quit()