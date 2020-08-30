import os
import pytest

from app1 import create_app


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    app = create_app()
    yield app


@pytest.fixture
def client(app):
    """A test client for the app."""
    yield app.test_client()


def tests_are_running_in_test_env():
    """Checks that tests are running in right environment."""
    assert os.getenv('FLASK_ENV') == 'testing'


def test_testing_set_true(app):
    """Test app instance has got testing flag equal True."""
    assert app.testing


def test_appstatus_view(client):
    """Test create_app render a view."""
    r = client.get('/appstatus')
    assert r.status_code == 200
    assert b'Flask is up and running in test config.' in r.data
