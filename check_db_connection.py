import pymysql.cursors
from fixture.db import DbFixture
from fixture.orm import ORMFixture
from model.group import Group

#lista kontaktów w określonej grupie i ich ilosc
db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = db.get_contacts_not_in_group(Group(id="471"))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass #db.destroy()

"""#drukowanie listy kontaktow oraz ich ilości
db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = db.get_contact_list()
    for item in l:
        print(item)
    print(len(l))
finally:
    pass #db.destroy()"""

"""#drukowanie listy grup oraz ich ilości
db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = db.get_group_list()
    for item in l:
        print(item)
    print(len(l))
finally:
    pass #db.destroy()"""
"""
# blok do weryfikacji połączenia z bazą danych
connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")

try:
    cursor = connection.cursor()
    cursor.execute("select * from group_list")
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close()
"""
"""#drukwoanie listy grup oraz ich ilości
db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    groups = db.get_group_list()
    for group in groups:
        print(group)
    print("Ilość grup: " + str(len(groups)))
finally:
    db.destroy()

#drukwoanie listy kontaktow oraz ich ilości
db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    contacts = db.get_contact_list()
    for contact in contacts:
        print(contact)
    print("Ilość kontaktów: " + str(len(contacts)))
finally:
    db.destroy()"""
""""
#drukowanie listy grup oraz ich ilości, weryfikacja czy połączenie działa
db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    groups = db.get_group_list()
    for group in groups:
        print(group)
    print(len(groups))
finally:
    db.destroy()"""