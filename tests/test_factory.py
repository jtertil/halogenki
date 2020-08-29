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


def test_testing_set_true(app):
    """Test app instance has got testing flag equal True."""
    assert app.testing


def test_app_factory_view(client):
    """Test create app render a view."""
    r = client.get(f'/app1')
    assert r.status_code == 200
    assert r.data == b'Flask is up and running in test config.'
