from selenium.webdriver.support.ui import Select


class Kontakty:
    def __init__(self, app):
        self.app = app

    def wypelnij_dane_kontaktowe_i_zapisz(self, contact):
        wd = self.app.wd
        self.otworz_strone_dodaj_kontakt()
        self.wypelnienie_danych_kontaktowych(contact)
        # zapisanie danych kontaktowych
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def wypelnienie_danych_kontaktowych(self, contact):
        wd = self.app.wd
        # wypełnienie danych kontaktowych
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.imie)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.imie2)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.nazwisko)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.inicjaly)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.firma)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.zwrot)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.adres)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.tel_domowy)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.tel_komorkowy)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.tel_praca)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.adres_mail2)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.strona_domowa)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.dzien_urodzin)
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.miesiac_urodzin)
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.rok_urodzenia)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.adres_mail2)

    def usuniecie_pierwszego_kontaktu(self):
        wd = self.app.wd
        self.app.otwarcie_strony_glownej()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.app.otwarcie_strony_glownej()

    def edycja_pierwszego_kontaktu(self, contact):
        wd = self.app.wd
        self.app.otwarcie_strony_glownej()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.wypelnienie_danych_kontaktowych(contact)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.app.otwarcie_strony_glownej()

    def otworz_strone_dodaj_kontakt(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
