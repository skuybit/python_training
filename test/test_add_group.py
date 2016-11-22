# -*- coding: utf-8 -*-
from model.group import Group


def _test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="abc", header="abc", footer="abc"))
    app.session.logout()


def _test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()


