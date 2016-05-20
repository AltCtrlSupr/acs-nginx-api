from test import app
import pytest
import re
import json

@pytest.fixture
def client(request):
    client = app.test_client()

    return client

# Testing homepage is printing anything..
def test_home_page(client):
    rv = client.get('/')
    # home should redirect to virtualhost
    assert rv._status_code == 302

# Testing posting a new virtual_host
def test_virtual_host_post(client):
    rv = client.post('/virtualhost')
    # This request should return error with no data
    error_regex = re.compile("(ERROR)")
    assert error_regex.search(rv.data) is not None
    assert rv._status_code == 400

    # Let's try the POST with some data
    data = {
        'name':'test',
        'ssl_cert':'LorMfaslkdjfalskfj',
        'ssl_key':'LorMfaslkdjfalskfj',
        'ssl_chain':'LorMfaslkdjfalskfj',
    }
    rv = client.post('/virtualhost', data=json.dumps(data), content_type='application/json')
    assert rv._status_code == 201
    assert 'test' in rv.data
    assert '_id' in rv.data

# Testing to get virtual_host collection
def test_virtual_host_index(client):
    rv = client.get('/virtualhost')
    assert rv._status_code == 200

    assert rv.headers[0] == ('Content-Type', 'application/json')
    assert 'test' in rv.data
    assert '_id' in rv.data

# Testing get only one virtual_host
def test_virtual_host_get(client):
    rv = client.get('/virtualhost')
    hosts = json.loads(rv.data)
    vhid = hosts[0]['_id']
    rv = client.get('/virtualhost/' + vhid)
    assert rv._status_code == 200

# Testing update a virtual_host
def test_virtual_host_put(client):
    rv = client.get('/virtualhost')
    hosts = json.loads(rv.data)
    vhid = hosts[0]['_id']
    data = {'name':'new_name'}
    rv = client.put('/virtualhost/' + vhid, data=json.dumps(data), content_type='application/json')
    assert rv._status_code == 200
    rv = client.get('/virtualhost/' + vhid)
    assert 'new_name' in rv.data

# Testing delete a virtual_host
def test_virtual_host_delete(client):
    rv = client.get('/virtualhost')
    hosts = json.loads(rv.data)
    vhid = hosts[0]['_id']
    rv = client.delete('/virtualhost/' + vhid)
    assert rv._status_code == 204
    rv = client.get('/virtualhost/' + vhid)
    assert rv._status_code == 404
