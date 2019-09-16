class Kontakty:
    def __init__(self, app):
        self.app = app

    def wypelnij_dane_kontaktowe_i_zapisz(self, contact):
        wd = self.app.wd
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

    def otworz_strone_z_kontaktami(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
