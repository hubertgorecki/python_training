# generator grup
from model.group import Group
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


# zwraca losowo generowane łańcuchy
def zwroc_ciag_znakow(prefix, maxlen):
    ciag_znakow = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(ciag_znakow) for i in range(random.randrange(maxlen))])


# zwraca losowe ciągi znaków dla nazwy, naglówków, stopek (5 razy pierwszą grupę generuje) + puste.
losowe_dane_testowe_grupy = [Group(nazwa="", naglowek="", stopka="")] + [
    Group(nazwa=zwroc_ciag_znakow("nazwa", 10), naglowek=zwroc_ciag_znakow("naglowek", 20),
          stopka=zwroc_ciag_znakow("stopka", 10)) for i in range(n)
]

# określenie lokalizacji pliku w którym zapisujemy dane. ".." przejście z poziomu generatora o 2 wyzej, następnie przejście do ścieżki /data.groups.json"
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
# otwieramy plik do zapisu (tryb "w"), nastęnie ustawiamy  dict - przypsianie własciwości które są dostepne w model/group w __init_
with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(losowe_dane_testowe_grupy))
