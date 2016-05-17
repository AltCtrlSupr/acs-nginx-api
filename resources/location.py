from resources.base import BaseResource
from flask import Flask, Blueprint
from flask.ext.restful import Api

app = Flask(__name__)
api_bp = Blueprint(__name__, __name__)
api = Api(api_bp)

class Location(BaseResource):
    def __init__(self):
        self.collection = 'location'
        super(Location, self).__init__()

api.add_resource(Location,
        '/location',
        '/location/<string:res_id>',
        endpoint='location')
