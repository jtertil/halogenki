import pytest

from app1 import create_app, Database


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    app = create_app()
    yield app


def test_database_config_in_app_config(app):
    assert app.config['DATABASE_CONFIG']


def test_database_initialize(app):
    db = Database(app.config['DATABASE_CONFIG'])
    assert db


def test_select_one_returns_tuple(app):
    db = Database(app.config['DATABASE_CONFIG'])
    q = "SELECT * FROM public.user;"
    r = db.select_one(q)
    assert isinstance(r, tuple)


def test_select_all_returns_list(app):
    db = Database(app.config['DATABASE_CONFIG'])
    q = "SELECT * FROM public.user;"
    r = db.select_all(q)
    assert isinstance(r, list)


def test_halogenki_in_user(app):
    db = Database(app.config['DATABASE_CONFIG'])
    q = "SELECT user_nick FROM public.user WHERE user_id=1;"
    r = db.select_one(q)
    assert r[0] == 'halogenki'


def test_user_no_exist_returns_none(app):
    db = Database(app.config['DATABASE_CONFIG'])
    q = "SELECT user_nick FROM public.user WHERE user_id=2;"
    r = db.select_one(q)
    assert not r


def test_insert_user(app):
    db = Database(app.config['DATABASE_CONFIG'])
    q = "INSERT INTO public.user (user_nick) VALUES ('test_user')"
    db.execute(q)
    q = "SELECT user_nick FROM public.user WHERE user_id=2;"
    r = db.select_one(q)
    assert r[0] == 'test_user'


