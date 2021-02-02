# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(login="admin", password="secret")
    app.group.create_contact(Contact(firstname="xghd", lastname="gddfgsd", company="jgfghj", address="jhdfgbxcb",
                                    telephone="5636456",
                                    mobile="2346765", tel_work="8765456", email="gfdfghbvcx", email_1="fsdfsdfg",
                                    www="gfdhfjdfg"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(login="admin", password="secret")
    app.group.create_contact(Contact(firstname="", lastname="", company="", address="", telephone="",
                                    mobile="", tel_work="", email="", email_1="",
                                    www=""))
    app.session.logout()