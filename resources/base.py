# -*- coding: utf-8 -*-
import json
from flask import Flask, Blueprint, current_app, jsonify, url_for, redirect, request, Response

from validators.mongo_validation import Validator

from database import mongo
from flask.ext.restful import Api, Resource
from bson.json_util import loads, dumps
from bson.objectid import ObjectId
from encoders.json_encoder import JSONEncoder

app = Flask(__name__)
api_bp = Blueprint(__name__, __name__)
api = Api(api_bp)

schema = dict()

# This is a base resource definition it works as a template for
# the real resources, it handles the basic CRUD
class BaseResource(Resource):

    collection = 'collection'

    def __init__(self):
        self.mongo = mongo
        if self.collection in current_app.config['DOMAIN']:
            self.schema = current_app.config['DOMAIN'][self.collection]['schema']
        else:
            self.schema = None

    # GET collection and resource specified by id
    def get(self, res_id = None):
        data = []

        if res_id:
            resource = self.mongo.db[self.collection].find_one({'_id': ObjectId(res_id)})
            data = json.loads(JSONEncoder().encode(resource))
        else:
            # Executing the query
            cursor = self.mongo.db[self.collection].find({}).limit(10)

            for item in cursor:
                data.append(json.loads(JSONEncoder().encode(item)))

        if data:
            return Response(json.dumps(data), mimetype='application/json')
        else:
            return Response([], status=404, mimetype='application/json')

    # POST a new resource
    def post(self):

        v = Validator(self.schema, self.collection)

        if not request.json:
            resp = jsonify({"response": "ERROR"})
            resp.status_code = 400

        elif not v.validate(request.json):
            resp = jsonify(v.errors)
            resp.status_code = 400

        else:
            self.mongo.db[self.collection].insert(request.json)
            resp = jsonify(json.loads(JSONEncoder().encode(request.json)))
            resp.status_code = 201

        return resp

    # Update a resource
    def put(self, res_id):
        v = Validator(self.schema, self.collection)

        data = request.get_json()
        resource = self.mongo.db[self.collection].update({'_id': ObjectId(res_id)}, {'$set': data})

        resp = jsonify(json.loads(JSONEncoder().encode(resource)))
        resp.status_code = 200

        return resp

    # Remove a resource
    def delete(self, res_id):
        self.mongo.db[self.collection].remove({'_id': ObjectId(res_id)})
        resp = jsonify([])
        resp.status_code = 204
        return resp
