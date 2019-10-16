from model.group import Group

stale_dane_testowe = [Group(nazwa="nazwa1", naglowek="naglowek1", stopka="stopka1"),
                      Group(nazwa="nazwa2", naglowek="naglowek2", stopka="stopka2")]













#
# # zwraca losowo generowane łańcuchy
# def zwroc_ciag_znakow(prefix, maxlen):
#     ciag_znakow = string.ascii_letters + string.digits + string.punctuation + " " * 10
#     return prefix + "".join([random.choice(ciag_znakow) for i in range(random.randrange(maxlen))])
#
#
# # zwraca losowe ciągi znaków dla nazwy, naglówków, stopek (5 razy pierwszą grupę generuje) + puste.
# losowe_dane_testowe_grupy = [Group(nazwa="", naglowek="", stopka="")] + [
#     Group(nazwa=zwroc_ciag_znakow("nazwa", 10), naglowek=zwroc_ciag_znakow("naglowek", 20),
#           stopka=zwroc_ciag_znakow("stopka", 10)) for i in range(5)
# ]
#
# # zwraca losowe ciągi znaków dla nazwy, naglówków, stopek - ich kombinacje.
# # dane_testowe = [Group(nazwa=nazwa, naglowek=naglowek, stopka=stopka)
# #                 for nazwa in [" ", zwroc_ciag_znakow("nazwa",10)]
# #                 for naglowek in [" ", zwroc_ciag_znakow("naglowek", 10)]
# #                 for stopka in [" ", zwroc_ciag_znakow("stopka", 10)]]
