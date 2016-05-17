from resources.base import BaseResource
from flask import Flask, Blueprint
from flask.ext.restful import Api
from flasgger.utils import swag_from

app = Flask(__name__)
api_bp = Blueprint(__name__, __name__)
api = Api(api_bp)

class Backend(BaseResource):
    def __init__(self):
        self.collection = 'backend'
        super(Backend, self).__init__()

    @swag_from('../doc/swagger/backend/get.yml')
    def get(self, res_id = None):
        return super(Backend, self).get(res_id)

    @swag_from('../doc/swagger/backend/post.yml')
    def post(self):
        return super(Backend, self).post()

    @swag_from('../doc/swagger/backend/put.yml')
    def put(self, res_id):
        return super(Backend, self).put(res_id)

    @swag_from('../doc/swagger/backend/delete.yml')
    def delete(self, res_id):
        return super(Backend, self).delete(res_id)

api.add_resource(Backend,
        '/backend',
        '/backend/<string:res_id>',
        endpoint='backend')
