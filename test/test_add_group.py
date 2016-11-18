# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture=Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def _test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="abc", header="abc", footer="abc"))
    app.session.logout()


def _test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()


