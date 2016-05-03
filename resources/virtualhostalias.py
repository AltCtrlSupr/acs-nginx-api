from resources.base import BaseResource
from flask import Flask, Blueprint
from flask.ext.restful import Api
from schemas import virtualhostalias

app = Flask(__name__)
api_bp = Blueprint(__name__, __name__)
api = Api(api_bp)

virtual_host_alias_schema = virtualhostalias.virtual_host_alias_schema

class VirtualHostAlias(BaseResource):
    def __init__(self):
        super(VirtualHostAlias, self).__init__()
        self.collection = 'virtualhostalias'
        self.schema = virtual_host_alias_schema

api.add_resource(VirtualHostAlias,
        '/virtualhostalias',
        '/virtualhostalias/<string:res_id>',
        endpoint='virtualhostalias')
