from resources.base import BaseResource
from flask import Flask, Blueprint
from flask.ext.restful import Api

app = Flask(__name__)
api_bp = Blueprint(__name__, __name__)
api = Api(api_bp)

schema = {
    'name': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 255,
        'required': True,
        # 'unique': True,
    },
}


class VirtualHostAlias(BaseResource):
    def __init__(self):
        super(VirtualHostAlias, self).__init__()
        self.collection = 'collection'
        self.schema = schema

api.add_resource(VirtualHostAlias, '/virtualhostalias', endpoint='virtualhostalias')
