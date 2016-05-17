from test import app
import pytest

@pytest.fixture
def client(request):
    client = app.test_client()

    return client

def test_doc_get(client):
    rv = client.get('/apidocs/index.html')
    # This request should return 200 code
    assert rv._status_code == 200
