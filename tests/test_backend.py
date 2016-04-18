from test import app
import pytest
import re
import json

@pytest.fixture
def client(request):
    client = app.test_client()

    return client

def test_backend_post(client):
    rv = client.post('/backend')
    # This request should return error with no data
    error_regex = re.compile("(ERROR)")
    assert error_regex.search(rv.data) is not None
    assert rv._status_code == 400

    # Let's try the POST with some data
    data = {
        'ip': '8.8.8.8',
        'ports': '80',
        'last_seen': '11/11/1985',
        'static': False,
    }
    rv = client.post('/backend', data=json.dumps(data), content_type='application/json')
    assert rv._status_code == 201
    assert '8.8.8.8' in rv.data

def test_backend_index(client):
    rv = client.get('/backend')
    assert rv._status_code == 200

    assert rv.headers[0] == ('Content-Type', 'application/json')
    assert '8.8.8.8' in rv.data
    assert '_id' in rv.data

def test_backend_get(client):
    rv = client.get('/backend')
    hosts = json.loads(rv.data)
    bid = hosts[0]['_id']
    rv = client.get('/backend/' + bid)
    assert rv._status_code == 200

def test_backend_remove(client):
    rv = client.get('/backend')
    hosts = json.loads(rv.data)
    bid = hosts[0]['_id']
    rv = client.delete('/backend/' + bid)
    assert rv._status_code == 204


