# -*- coding: utf-8 -*-
from flask import Flask, Blueprint
from flask.ext.restful import Api
from resources.base import BaseResource

app = Flask(__name__)
api_bp = Blueprint(__name__, __name__)
api = Api(api_bp)

virtual_host_schema = {
    'name': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 255,
        'required': True,
        # 'unique': True,
    },
    'ssl_cert': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 255,
        'required': False,
    },
    'ssl_key': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 255,
        'required': False,
    },
    'ssl_chain': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 255,
        'required': False,
    },
    'ports_plain': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 255,
        'required': False,
    },
    'ports_ssl': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 255,
        'required': False,
    },
    'virtual_host_alias': {
	'type': 'string',
        'minlength': 1,
        'maxlength': 255,
        'required': False,
    }
}

class VirtualHost(BaseResource):
    def __init__(self):
        super(VirtualHost, self).__init__()
        self.collection = 'virtualhost'
        self.schema = virtual_host_schema

api.add_resource(VirtualHost,
        "/virtualhost",
        "/virtualhost/<string:res_id>",
        endpoint="virtualhosts")
