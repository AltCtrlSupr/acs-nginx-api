# -*- coding: utf-8 -*-
import json
from flask import Flask, Blueprint, current_app, jsonify, url_for, redirect, request, Response
from cerberus import Validator
from database import mongo
from flask.ext.restful import Api, Resource
from bson.json_util import loads, dumps

app = Flask(__name__)
api_bp = Blueprint(__name__, __name__)
api = Api(api_bp)

schema = dict()

class BaseResource(Resource):
    def __init__(self):
        self.mongo = mongo
        self.collection = 'collection'
        self.schema = schema

    def get(self):
        data = []

        cursor = self.mongo.db.virtualhost.find({}, {"_id": 0, "update_time": 0}).limit(10)

        for virtualhost in cursor:
            data.append(virtualhost)

        return Response(json.dumps(data),  mimetype='application/json')

    def post(self):

        v = Validator(virtual_host_schema)

        if not request.json:
            resp = jsonify({"response": "ERROR"})
            resp.status_code = 400

        elif not v.validate(request.json):
            resp = jsonify(v.errors)
            resp.status_code = 400

        else:
            self.mongo.db.virtualhost.insert(request.json)
            resp = jsonify(json.loads(dumps(request.json)))
            resp.status_code = 201

        return resp

    def put(self, slug):
        data = request.get_json()
        self.mongo.db.virtualhost.update({'slug': slug}, {'$set': data})
        return redirect(url_for("virtualhost.virtualhosts"))

    def delete(self, slug):
        self.mongo.db.virtualhost.remove({'slug': slug})
        return redirect(url_for("virtualhost.virtualhosts"))
