# -*- coding: utf-8 -*-

from flask import Flask, Blueprint, current_app, jsonify, url_for, redirect, request
from database import mongo
import json
from flask.ext.restful import Api, Resource

app = Flask(__name__)
api_bp = Blueprint(__name__, __name__)
api = Api(api_bp)

class VirtualHost(Resource):
    def __init__(self):
        self.mongo = mongo

    def get(self):
        data = []

        cursor = self.mongo.db.virtualhost.find({}, {"_id": 0, "update_time": 0}).limit(10)

        for virtualhost in cursor:
            data.append(virtualhost)

        json.dumps(data)

    def post(self):
        print("post")
        data = request.get_json()
        print(data)
        if not data:
            data = {"response": "ERROR"}
            resp = jsonify(data)
            resp.status_code = 400
            return resp
        else:
            self.mongo.db.virtualhost.insert(data)

        return redirect(url_for("virtualhost.virtualhosts"))

    def put(self, slug):
        data = request.get_json()
        self.mongo.db.virtualhost.update({'slug': slug}, {'$set': data})
        return redirect(url_for("virtualhost.virtualhosts"))

    def delete(self, slug):
        self.mongo.db.virtualhost.remove({'slug': slug})
        return redirect(url_for("virtualhost.virtualhosts"))

api.add_resource(VirtualHost, "/virtualhost", endpoint="virtualhosts")
