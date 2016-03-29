from main import app
import pytest
import re
import tempfile

@pytest.fixture
def client(request):
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True
    client = app.test_client()

    return client

def test_home_page(client):
    rv = client.get('/')
    # home should redirect to virtualhost
    assert rv._status_code == 302

def test_virtual_host_post(client):
    rv = client.post('/virtualhost')
    # This request should return error with no data
    error_regex = re.compile("(ERROR)")
    assert error_regex.search(rv.data) is not None
    assert rv._status_code == 400


def test_virtual_host_index(client):
    rv = client.get('/virtualhost')
    assert rv._status_code == 200

    assert rv.headers[0] == ('Content-Type', 'application/json')

    # print vars(rv)
    # assert 1 != 1
    # assert 'whatever' in rv.data

