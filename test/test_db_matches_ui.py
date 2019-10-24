from model.group import Group

#test porownujacy liste grup na stronie z lista grup w bazie
def test_group_list(app, db):
    ui_list = app.group.zwroc_liste_grup()
    #w funkcji clean usuwane są wszystkie zbędne spacje z początku i końca ciągu znakow
    def clean(group):
        return Group(id=group.id, nazwa=group.nazwa.strip())
    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)