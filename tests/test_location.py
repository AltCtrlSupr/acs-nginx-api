from test import app
import pytest
import re
import json

@pytest.fixture
def client(request):
    client = app.test_client()

    return client

def test_location_post(client):
    rv = client.post('/location')
    # This request should return error with no data
    error_regex = re.compile("(ERROR)")
    assert error_regex.search(rv.data) is not None
    assert rv._status_code == 400

    # Let's try the POST with some data
    data = {'path':'test'}
    rv = client.post('/location', data=json.dumps(data), content_type='application/json')
    assert rv._status_code == 201
    assert 'test' in rv.data

def test_location_index(client):
    rv = client.get('/location')
    assert rv._status_code == 200

    assert rv.headers[0] == ('Content-Type', 'application/json')
    assert 'test' in rv.data
    assert '_id' in rv.data

def test_location_get(client):
    rv = client.get('/location')
    hosts = json.loads(rv.data)
    lid = hosts[0]['_id']
    rv = client.get('/location/' + lid)
    assert rv._status_code == 200

def test_location_remove(client):
    rv = client.get('/location')
    hosts = json.loads(rv.data)
    lid = hosts[0]['_id']
    rv = client.delete('/location/' + lid)
    assert rv._status_code == 204


