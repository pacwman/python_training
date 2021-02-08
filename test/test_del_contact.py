from model.contact import Contact


def test_delete_first_contact(app):
    app.session.login(login="admin", password="secret")
    app.group.create_contact(Contact(firstname="xghd", lastname="gddfgsd", company="jgfghj", address="jhdfgbxcb",
                                     telephone="5636456",
                                     mobile="2346765", tel_work="8765456", email="gfdfghbvcx", email_1="fsdfsdfg",
                                     www="gfdhfjdfg"))
    app.group.delete_first_contact()
    app.session.logout()
