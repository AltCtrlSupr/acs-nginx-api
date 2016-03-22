import os
import main
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, main.app.config['DATABASE'] = tempfile.mkstemp()
        main.app.config['TESTING'] = True
        self.app = main.app.test_client()
        # main.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(main.app.config['DATABASE'])

    def test_virtual_host_index(self):
        rv = self.app.get('/')
        assert 'whatever' in rv.data

if __name__ == '__main__':
    unittest.main()
