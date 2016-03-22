# -*- coding: utf-8 -*-

from flask import Flask, jsonify, url_for, redirect, request
from flask.ext.pymongo import PyMongo
from flask.ext.restful import Api, Resource

app = Flask(__name__)
api = Api(app)

from resources.virtualhost import VirtualHost
api.add_resource(VirtualHost, "/api", endpoint="virtualhosts")

@app.route('/')
def index(): return redirect(url_for('virtualhosts'))

if __name__ == "__main__":
    app.config.from_object('config.Development')
    app.run(debug=True)
