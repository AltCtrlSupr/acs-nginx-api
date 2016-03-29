from main import app
import pytest
import re
import json
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

    # Let's try the POST with some data
    data = {'name':'test'}
    rv = client.post('/virtualhost', data=json.dumps(data), content_type='application/json')
    assert rv._status_code == 201
    print(rv.data)

# def test_virtual_host_ge(client):
    # rv = client.get('/virtualhost/1')
    # assert rv._status_code == 200


def test_virtual_host_index(client):
    rv = client.get('/virtualhost')
    assert rv._status_code == 200

    assert rv.headers[0] == ('Content-Type', 'application/json')

    assert 'test' in rv.data

