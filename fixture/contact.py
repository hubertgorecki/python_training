from selenium.webdriver.support.ui import Select
from model.contact import Contact


class Kontakty:
    def __init__(self, app):
        self.app = app

    def wypelnij_dane_kontaktowe_i_zapisz(self, contact):
        wd = self.app.wd
        self.otworz_strone_dodaj_kontakt()
        self.wypelnienie_formularza_danymi_kontaktu(contact)
        # zapisanie danych kontaktowych
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.contact_cache = None

    # def wypelnienie_danych_kontaktowych(self, contact):
    #     wd = self.app.wd
    #     # wypełnienie danych kontaktowych
    #     wd.find_element_by_name("firstname").click()
    #     wd.find_element_by_name("firstname").clear()
    #     wd.find_element_by_name("firstname").send_keys(contact.imie)
    #     wd.find_element_by_name("middlename").click()
    #     wd.find_element_by_name("middlename").clear()
    #     wd.find_element_by_name("middlename").send_keys(contact.imie2)
    #     wd.find_element_by_name("lastname").click()
    #     wd.find_element_by_name("lastname").clear()
    #     wd.find_element_by_name("lastname").send_keys(contact.nazwisko)
    #     wd.find_element_by_name("nickname").click()
    #     wd.find_element_by_name("nickname").clear()
    #     wd.find_element_by_name("nickname").send_keys(contact.inicjaly)
    #     wd.find_element_by_name("company").click()
    #     wd.find_element_by_name("company").clear()
    #     wd.find_element_by_name("company").send_keys(contact.firma)
    #     wd.find_element_by_name("title").click()
    #     wd.find_element_by_name("title").clear()
    #     wd.find_element_by_name("title").send_keys(contact.zwrot)
    #     wd.find_element_by_name("address").click()
    #     wd.find_element_by_name("address").click()
    #     wd.find_element_by_name("address").clear()
    #     wd.find_element_by_name("address").send_keys(contact.adres)
    #     wd.find_element_by_name("home").click()
    #     wd.find_element_by_name("home").clear()
    #     wd.find_element_by_name("home").send_keys(contact.tel_domowy)
    #     wd.find_element_by_name("mobile").click()
    #     wd.find_element_by_name("mobile").clear()
    #     wd.find_element_by_name("mobile").send_keys(contact.tel_komorkowy)
    #     wd.find_element_by_name("work").click()
    #     wd.find_element_by_name("work").clear()
    #     wd.find_element_by_name("work").send_keys(contact.tel_praca)
    #     wd.find_element_by_name("email2").click()
    #     wd.find_element_by_name("email2").clear()
    #     wd.find_element_by_name("email2").send_keys(contact.adres_mail2)
    #     wd.find_element_by_name("homepage").click()
    #     wd.find_element_by_name("homepage").clear()
    #     wd.find_element_by_name("homepage").send_keys(contact.strona_domowa)
    #     wd.find_element_by_name("bmonth").click()
    #     Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.miesiac_urodzin)
    #     wd.find_element_by_name("byear").click()
    #     wd.find_element_by_name("byear").clear()
    #     wd.find_element_by_name("byear").send_keys(contact.rok_urodzenia)
    #     wd.find_element_by_name("address2").click()
    #     wd.find_element_by_name("address2").clear()
    #     wd.find_element_by_name("address2").send_keys(contact.adres_mail2)

    def wypelnienie_formularza_danymi_kontaktu(self, contact):
        wd = self.app.wd
        self.zmien_tresc_danego_pola_kontakty("firstname", contact.imie)
        self.zmien_tresc_danego_pola_kontakty("middlename", contact.imie2)
        self.zmien_tresc_danego_pola_kontakty("lastname", contact.nazwisko)
        self.zmien_tresc_danego_pola_kontakty("nickname", contact.inicjaly)
        self.zmien_tresc_danego_pola_kontakty("company", contact.firma)
        self.zmien_tresc_danego_pola_kontakty("title", contact.zwrot)
        self.zmien_tresc_danego_pola_kontakty("address", contact.adres)
        self.zmien_tresc_danego_pola_kontakty("home", contact.tel_domowy)
        self.zmien_tresc_danego_pola_kontakty("mobile", contact.tel_komorkowy)
        self.zmien_tresc_danego_pola_kontakty("work", contact.tel_praca)
        self.zmien_tresc_danego_pola_kontakty("fax", contact.tel_fax)
        self.zmien_tresc_danego_pola_kontakty("email", contact.adres_mail)
        self.zmien_tresc_danego_pola_kontakty("email2", contact.adres_mail2)
        self.zmien_tresc_danego_pola_kontakty("homepage", contact.strona_domowa)
        self.zmien_tresc_danego_pola_kontakty_listy("bday", contact.dzien_urodzin)
        self.zmien_tresc_danego_pola_kontakty_listy("bmonth", contact.miesiac_urodzin)
        self.zmien_tresc_danego_pola_kontakty("byear", contact.rok_urodzenia)
        self.zmien_tresc_danego_pola_kontakty("address2", contact.alrternatywny_adres)

    def zmien_tresc_danego_pola_kontakty_listy(self, nazwa_pola, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(nazwa_pola).click()
            Select(wd.find_element_by_name(nazwa_pola)).select_by_visible_text(text)

    def zmien_tresc_danego_pola_kontakty(self, nazwa_pola, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(nazwa_pola).click()
            wd.find_element_by_name(nazwa_pola).clear()
            wd.find_element_by_name(nazwa_pola).send_keys(text)

    def usuniecie_pierwszego_kontaktu(self):
        wd = self.app.wd
        self.app.otwarcie_strony_glownej()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.app.otwarcie_strony_glownej()
        self.contact_cache = None

    def usuniecie_losowego_kontaktu(self, index):
        wd = self.app.wd
        self.app.otwarcie_strony_glownej()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.app.otwarcie_strony_glownej()
        self.contact_cache = None

    def edycja_pierwszego_kontaktu(self, contact):
        wd = self.app.wd
        self.app.otwarcie_strony_glownej()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.wypelnienie_formularza_danymi_kontaktu(contact)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.app.otwarcie_strony_glownej()
        self.contact_cache = None

    def edycja_losowego_kontaktu(self, contact, index):
        wd = self.app.wd
        self.app.otwarcie_strony_glownej()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.wypelnienie_formularza_danymi_kontaktu(contact)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.app.otwarcie_strony_glownej()
        self.contact_cache = None

    def otworz_strone_dodaj_kontakt(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def licznik_checkboxow_kontakty(self):
        wd = self.app.wd
        self.app.otwarcie_strony_glownej()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def zwroc_liste_kontaktow(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.otwarcie_strony_glownej()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                wiersz = element.find_elements_by_tag_name("td")
                id = element.find_element_by_name("selected[]").get_attribute("value")
                nazwisko = wiersz[1].text
                imie = wiersz[2].text
                wszystkie_telefony = wiersz[5].text.splitlines()
                self.contact_cache.append(
                    Contact(imie=imie, nazwisko=nazwisko, id=id, tel_domowy=wszystkie_telefony[0],
                            tel_praca=wszystkie_telefony[2], tel_komorkowy=wszystkie_telefony[1]))

        return list(self.contact_cache)

    def otworz_edycje_kontaktu_o_indexie(self, index):
        wd = self.app.wd
        self.app.otwarcie_strony_glownej()
        wiersz = wd.find_elements_by_name("entry")[index]
        komorka = wiersz.find_elements_by_tag_name("td")[7]
        komorka.find_element_by_tag_name("a").click()

    def otworz_podglad_kontaktu_o_indexie(self, index):
        wd = self.app.wd
        self.app.otwarcie_strony_glownej()
        wiersz = wd.find_elements_by_name("entry")[index]
        komorka = wiersz.find_elements_by_tag_name("td")[6]
        komorka.find_element_by_tag_name("a").click()

    def info_o_konktakcie_w_edycji(self, index):
        wd = self.app.wd
        self.otworz_edycje_kontaktu_o_indexie(index)
        imie = wd.find_element_by_name("firstname").get_attribute("value")
        nazwisko = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        tel_domowy = wd.find_element_by_name("home").get_attribute("value")
        tel_komorkowy = wd.find_element_by_name("mobile").get_attribute("value")
        tel_praca = wd.find_element_by_name("work").get_attribute("value")
        tel_fax = wd.find_element_by_name("fax").get_attribute("value")
        return Contact(imie=imie, nazwisko=nazwisko, id=id, tel_domowy=tel_domowy, tel_praca=tel_praca,
                       tel_komorkowy=tel_komorkowy)
