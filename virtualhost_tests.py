from main import app
import pytest
import tempfile

@pytest.fixture
def client(request):
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True
    client = app.test_client()
    # with app.app_context():
        # init_db()

    # def teardown():
        # os.close(db_fd)
        # os.unlink(app.config['DATABASE'])
    # request.addfinalizer(teardown)

    return client

def test_virtual_host_index(client):
    rv = client.get('/virtualhost')
    assert rv._status_code == 200

    # print vars(rv)
    # assert 1 != 1
    # assert 'whatever' in rv.data

