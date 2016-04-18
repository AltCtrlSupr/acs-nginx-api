from resources.base import BaseResource
from flask import Flask, Blueprint
from flask.ext.restful import Api

app = Flask(__name__)
api_bp = Blueprint(__name__, __name__)
api = Api(api_bp)

location_schema = {
    'path': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 255,
        'required': True,
        # 'unique': True,
    },
}

class Location(BaseResource):
    def __init__(self):
        super(Location, self).__init__()
        self.collection = 'location'
        self.schema = location_schema

api.add_resource(Location,
        '/location',
        '/location/<string:res_id>',
        endpoint='location')
