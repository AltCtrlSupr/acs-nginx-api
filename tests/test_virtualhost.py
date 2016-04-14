from test import app
import pytest
import re
import json

@pytest.fixture
def client(request):
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
    assert 'test' in rv.data
    assert '_id' in rv.data

def test_virtual_host_get(client):
    rv = client.get('/virtualhost')
    hosts = json.loads(rv.data)
    vhid = hosts[0]['_id']
    rv = client.get('/virtualhost/' + vhid)
    assert rv._status_code == 200

def test_virtual_host_index(client):
    rv = client.get('/virtualhost')
    assert rv._status_code == 200

    assert rv.headers[0] == ('Content-Type', 'application/json')
    assert 'test' in rv.data
    assert '_id' in rv.data

