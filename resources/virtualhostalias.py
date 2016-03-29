from resources.base import BaseResource
from flask import Flask, Blueprint
from flask.ext.restful import Api

app = Flask(__name__)
api_bp = Blueprint(__name__, __name__)
api = Api(api_bp)

schema = dict()

class VirtualHostAlias(BaseResource):
    def __init__(self):
        super(VirtualHostAlias, self).__init__()
        self.collection = 'collection'
        self.schema = schema

api.add_resource(VirtualHostAlias, '/virtualhostalias', endpoint='virtualhostalias')
