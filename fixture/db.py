import mysql.connector
from model.group import Group
from model.contact import Contact


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password,
                                                  autocommit=True)

    def get_group_list(self):
        cursor = self.connection.cursor()
        list = []
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), nazwa=name, naglowek=header, stopka=footer))

        finally:
            cursor.close()

        return list

    def get_contact_list(self):
        cursor = self.connection.cursor()
        list = []
        try:
            cursor.execute(
                "select id, firstname, middlename, lastname, nickname, company, title, address, home, mobile, work,"
                " fax, email, email2, homepage, bday, bmonth, byear, phone2"
                " from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, middlename, lastname, nickname, company, title, address, home, mobile, work, fax, email,
                 email2, homepage, bday, bmonth, byear, phone2) = row
                list.append(Contact(id=str(id), imie=firstname, imie2=middlename, nazwisko=lastname, inicjaly=nickname,
                                    firma=company, zwrot=title, adres=address, tel_domowy=home, tel_komorkowy=mobile,
                                    tel_praca=work,
                                    tel_fax=fax, adres_mail=email, adres_mail2=email2, strona_domowa=homepage,
                                    dzien_urodzin=bday, miesiac_urodzin=bmonth, rok_urodzenia=byear,
                                    tel_domowy2=phone2))

        finally:
            cursor.close()

        return list

    def destroy(self):
        self.connection.close()
