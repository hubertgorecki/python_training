# generator kontaktów
from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contact", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

nazwy_miesiecy = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                  "November", "December"]


def zwroc_ciag_znakow(prefix, maxlen):
    ciag_znakow = string.ascii_letters + string.digits + " " * 4
    return prefix + "".join([random.choice(ciag_znakow) for i in range(random.randrange(maxlen))])


def zwroc_numer_tel(prefix, maxlen):
    numer_telefonu = string.digits
    return prefix + "+ " + "".join([random.choice(numer_telefonu) for i in range(random.randrange(maxlen))])


def zwroc_email(prefix, maxlen):
    adres_mail = string.ascii_lowercase + string.digits
    domena = "".join([random.choice(string.ascii_lowercase) for i in range(random.randrange(5))])
    return prefix + "".join([random.choice(adres_mail) for i in range(random.randrange(maxlen))]) + "@" + domena + ".pl"


def zwroc_adres_www(prefix, maxlen):
    adres_strony_www = string.ascii_lowercase
    losowy = "".join([random.choice(adres_strony_www) for i in range(random.randrange(maxlen))])
    return prefix + "www." + losowy + ".pl"


def zwroc_dzien_urodzin():
    dzien = random.randint(1, 31)
    return str(dzien)


def zwroc_miesiac_urodzin():
    miesiac = random.choice(nazwy_miesiecy)
    return miesiac


def zwroc_rok_urodzin():
    rok_biezacy = random.randint(1920, 2000)
    return str(rok_biezacy)


# zwraca losowe ciągi znaków dla wskazanych nazw + puste.
losowe_dane_testowe_kontakt = [
                                  Contact(imie="", imie2="",
                                          nazwisko="",
                                          inicjaly="",
                                          firma="", zwrot="",
                                          adres="",
                                          tel_domowy="",
                                          tel_komorkowy="",
                                          tel_praca="",
                                          adres_mail="",
                                          adres_mail2="",
                                          adres_mail3="",
                                          strona_domowa="",
                                          dzien_urodzin="",
                                          miesiac_urodzin="",
                                          rok_urodzenia="",
                                          alrternatywny_adres="",
                                          tel_domowy2="")] + \
                              [
                                  Contact(imie=zwroc_ciag_znakow("imie: ", 8), imie2=zwroc_ciag_znakow("imie2: ", 8),
                                          nazwisko=zwroc_ciag_znakow("nazwisko: ", 10),
                                          inicjaly=zwroc_ciag_znakow("inicjały: ", 2),
                                          firma=zwroc_ciag_znakow("firma: ", 6), zwrot=zwroc_ciag_znakow("zwrot: ", 2),
                                          adres=zwroc_ciag_znakow("adres: ", 10),
                                          tel_domowy=zwroc_numer_tel("Tel_dom: ", 9),
                                          tel_komorkowy=zwroc_numer_tel("Tel_kom: ", 9),
                                          tel_praca=zwroc_numer_tel("Tel_prac: ", 9),
                                          tel_fax=zwroc_numer_tel("Tel_fax: ", 9),
                                          adres_mail=zwroc_email("mail: ", 10),
                                          adres_mail2=zwroc_email("mail2: ", 10),
                                          adres_mail3=zwroc_email("mail3: ", 10),
                                          strona_domowa=zwroc_adres_www("str_dom: ", 20),
                                          dzien_urodzin=zwroc_dzien_urodzin(),
                                          miesiac_urodzin=zwroc_miesiac_urodzin(),
                                          rok_urodzenia=zwroc_rok_urodzin(),
                                          alrternatywny_adres=zwroc_ciag_znakow("adres2: ", 10),
                                          tel_domowy2=zwroc_numer_tel("Tel_dom2: ", 9)
                                          ) for i in range(5)]

# określenie lokalizacji pliku w którym zapisujemy dane. ".." przejście z poziomu generatora o 2 wyzej, następnie przejście do ścieżki /data.contacts.json"
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
# otwieramy plik do zapisu (tryb "w"), nastęnie ustawiamy  dict - przypsianie własciwości które są dostepne w model/group w __init_
with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(losowe_dane_testowe_kontakt))
