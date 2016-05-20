from test import app
from generators.nginx_conf_generator import NginxConfGenerator
import pytest

def test_write_file():
    with app.app_context():
        generator = NginxConfGenerator()
        generator.generate()
        assert True == True
