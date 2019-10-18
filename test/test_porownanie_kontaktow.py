import re


def test_telefonow_na_stronie_glownej(app):
    kontakt_ze_strony_glownej = app.contact.zwroc_liste_kontaktow()[0]
    kontakt_ze_strony_edycji = app.contact.info_o_konktakcie_w_edycji(0)
    assert kontakt_ze_strony_glownej.wszystkie_tel_na_stronie_glownej == sklej_tel_widoczne_w_edycji(
        kontakt_ze_strony_edycji)


def test_telefonow_na_podgladzie_kontaktu(app):
    kontakt_z_podgladu_strony = app.contact.info_o_konktakcie_w_podgladzie(0)
    kontakt_ze_strony_edycji = app.contact.info_o_konktakcie_w_edycji(0)
    assert kontakt_z_podgladu_strony.tel_domowy == kontakt_ze_strony_edycji.tel_domowy
    assert kontakt_z_podgladu_strony.tel_komorkowy == kontakt_ze_strony_edycji.tel_komorkowy
    assert kontakt_z_podgladu_strony.tel_praca == kontakt_ze_strony_edycji.tel_praca
    assert kontakt_z_podgladu_strony.tel_domowy2 == kontakt_ze_strony_edycji.tel_domowy2


def test_porownanie_imie_nazwisko(app):
    kontakt_z_podgladu_strony = app.contact.zwroc_liste_kontaktow()[0]
    kontakt_ze_strony_edycji = app.contact.info_o_konktakcie_w_edycji(0)
    assert kontakt_z_podgladu_strony.imie == kontakt_ze_strony_edycji.imie
    assert kontakt_z_podgladu_strony.nazwisko == kontakt_ze_strony_edycji.nazwisko


def test_porownanie_adresu(app):
    kontakt_z_podgladu_strony = app.contact.zwroc_liste_kontaktow()[0]
    kontakt_ze_strony_edycji = app.contact.info_o_konktakcie_w_edycji(0)
    assert kontakt_z_podgladu_strony.adres == kontakt_ze_strony_edycji.adres


def test_porownanie_adresow_mail(app):
    kontakt_z_podgladu_strony = app.contact.zwroc_liste_kontaktow()[0]
    kontakt_ze_strony_edycji = app.contact.info_o_konktakcie_w_edycji(0)
    assert kontakt_z_podgladu_strony.wszystkie_adresy_mail == sklej_adresy_mail_widoczne_w_edycji(
        kontakt_ze_strony_edycji)
    print(kontakt_z_podgladu_strony.wszystkie_adresy_mail)
    print(sklej_adresy_mail_widoczne_w_edycji(kontakt_ze_strony_edycji))


# czyści ciąg znaków z pustych znaków oraz z - spacji i nawiasów
def czysc(s):
    return re.sub("[() -]", "", s)


def sklej_tel_widoczne_w_edycji(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: czysc(x),
                                filter(lambda x: x is not None,
                                       [contact.tel_domowy, contact.tel_komorkowy, contact.tel_praca,
                                        contact.tel_domowy2]))))


def sklej_adresy_mail_widoczne_w_edycji(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.adres_mail, contact.adres_mail2, contact.adres_mail3])))
