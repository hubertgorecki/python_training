from pony.orm import *
from _datetime import datetime
from model.group import Group
from model.contact import Contact
from pymysql.converters import decoders

class ORMFixture:
    db = Database()
    #tworzymy klase zawierajacą właściwowści tabeli w bazie, przyporządkować je należy do pól tabeli, czyli id, name itd)
    class ORMGroup(db.Entity):
        _table_ = "group_list" #nazwa tabeli
        id = PrimaryKey(int, column="group_id")
        nazwa = Optional(str, column="group_name")
        naglowek = Optional(str, column="group_header")
        stopka = Optional(str, column="group_footer")
        contacts = Set(lambda: ORMFixture.ORMContact, table="address_in_groups", column="id", reverse="groups", lazy=True)

    class ORMContact(db.Entity):
        _table_ = "addressbook"
        id = PrimaryKey(int, column="id")
        imie = Optional(str, column="firstname")
        nazwisko = Optional(str, column="lastname")
        deprecated = Optional(datetime, column="deprecated")
        groups = Set(lambda: ORMFixture.ORMGroup,  table="address_in_groups", column="group_id", reverse="contacts", lazy=True)

    def __init__(self, host, name, user, password):
        self.db.bind("mysql", host=host, database=name, user=user, password=password)
        #self.db.bind("mysql", host=host, database=name, user=user, password=password, conv=decoders)
        self.db.generate_mapping()
        sql_debug(True)
    #metoda konwertująca grupy zgodnie z modelem, która przyjmuje jako parametr listy grup

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), nazwa=group.nazwa, naglowek=group.naglowek, stopka=group.stopka)
        return list(map(convert, groups))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), imie=contact.imie, nazwisko=contact.nazwisko)
        return list(map(convert, contacts))

    #otwieramy sesje
    @db_session
    #tworzymy listę grup
    def get_group_list(self):
        # zamiast @db_session można użyć with db_session w tym miejscu. Sesja się sama otwiera i zamyka
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    #otwieramy sesje
    @db_session
    #tworzymy listę kontaktow
    def get_contact_list(self):
        # zamiast @db_session można użyć with db_session w tym miejscu. Sesja się sama otwiera i zamyka
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))

    @db_session
    def get_contacts_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(orm_group.contacts)

    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(
            select(c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group not in c.groups))