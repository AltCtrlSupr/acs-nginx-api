# -*- coding: utf-8 -*-

from flask import current_app, jsonify, url_for, redirect, request
from flask_pymongo import PyMongo
from flask_restful import Resource

class VirtualHost(Resource):
    def __init__(self):
        self.mongo = PyMongo(current_app)

    def get(self, slug):
        data = []

        cursor = mongo.db.virtualhost.find({}, {"_id": 0, "update_time": 0}).limit(10)

        for virtualhost in cursor:
            print(virtualhost)
            data.append(virtualhost)

        return jsonify(data)

    def post(self):
        data = request.get_json()
        if not data:
            data = {"response": "ERROR"}
            return jsonify(data)
        else:
            #if mongo.db.virtualhost.find_one({"slug": slug}):
                #return {"response": "student already exists."}
            #else:
            mongo.db.virtualhost.insert(data)

        return redirect(url_for("virtualhosts"))

    def put(self, slug):
        data = request.get_json()
        mongo.db.virtualhost.update({'slug': slug}, {'$set': data})
        return redirect(url_for("virtualhosts"))

    def delete(self, slug):
        mongo.db.virtualhost.remove({'slug': slug})
        return redirect(url_for("virtualhosts"))
