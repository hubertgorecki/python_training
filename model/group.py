from sys import maxsize

class Group:
    def __init__(self, nazwa=None, naglowek=None, stopka=None, id=None):
        self.nazwa = nazwa
        self.naglowek = naglowek
        self.stopka = stopka
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.nazwa)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.nazwa == other.nazwa

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize