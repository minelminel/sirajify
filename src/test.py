import pytest
import json
from flask import json, Response
from bs4 import BeautifulSoup
from werkzeug.utils import cached_property
from app import create_app

class TestingResponse(Response):

    @cached_property
    def json(self):
        assert self.mimetype == 'application/x-www-form-urlencoded'
        return json.loads(self.data)


@pytest.yield_fixture(scope='session')
def app():
    settings = dict(
        env='testing',
        testing=True,
        debug=True,
    )
    application = create_app(settings)
    application.response_class = TestingResponse
    ctx = application.app_context()
    ctx.push()
    yield application
    ctx.pop()


@pytest.fixture(scope='session')
def client(app):
    return app.test_client()

# ===== Begin tests =====
def test_app_homepage_loads(client):
    response = client.get('/')
    assert response.status_code == 200


def test_app_404_redirection(client):
    response = client.get('/does-not-exist')
    assert response.status_code != 404


def test_app_form_submission(client):
    key,msg = 'FormText','ipsum lorem'
    mimetype = 'application/x-www-form-urlencoded'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        key: msg
    }
    url = '/'
    response = client.post(url, data=data, headers=headers)
    assert response.status_code == 200
    soup = BeautifulSoup(response.data, 'html.parser')
    assert soup.find(id=key).text == msg
