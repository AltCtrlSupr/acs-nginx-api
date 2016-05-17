from resources.base import BaseResource
from flask import Flask, Blueprint
from flask.ext.restful import Api

app = Flask(__name__)
api_bp = Blueprint(__name__, __name__)
api = Api(api_bp)

class VirtualHostAlias(BaseResource):
    def __init__(self):
        self.collection = 'virtualhostalias'
        super(VirtualHostAlias, self).__init__()

api.add_resource(VirtualHostAlias,
        '/virtualhostalias',
        '/virtualhostalias/<string:res_id>',
        endpoint='virtualhostalias')
