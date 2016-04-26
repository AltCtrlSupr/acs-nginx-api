# -*- coding: utf-8 -*-
from flask import Flask, Blueprint
from flask.ext.restful import Api
from resources.base import BaseResource
from schemas import virtualhost
from flasgger.utils import swag_from

virtual_host_schema = virtualhost.virtual_host_schema

app = Flask(__name__)
api_bp = Blueprint(__name__, __name__)
api = Api(api_bp)

class VirtualHost(BaseResource):
    def __init__(self):
        super(VirtualHost, self).__init__()
        self.collection = 'virtualhost'
        self.schema = virtual_host_schema

    @swag_from('../doc/swagger/virtualhost/get.yml')
    def get(self, res_id = None):
        return super(VirtualHost, self).get(res_id)

    @swag_from('../doc/swagger/virtualhost/post.yml')
    def post(self):
        return super(VirtualHost, self).post()

api.add_resource(VirtualHost,
        "/virtualhost",
        "/virtualhost/<string:res_id>",
        endpoint="virtualhosts")
