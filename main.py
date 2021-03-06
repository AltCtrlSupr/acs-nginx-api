# -*- coding: utf-8 -*-
from flask import Flask, url_for, redirect
from database import mongo
import pkgutil

app = Flask(__name__)

# Loading dynamically the resources
resources_dir = 'resources'
for importer, package_name, _ in pkgutil.iter_modules([resources_dir]):
    module = importer.find_module(package_name).load_module('%s' % (package_name))
    if hasattr(module, 'api_bp'):
        app.register_blueprint(getattr(module, 'api_bp'))

# Default home endpoint
@app.route('/')
def index():
    return redirect(url_for('virtualhost.virtualhosts'))

if __name__ == "__main__":
    app.config.from_object('config.Development')
    app.run(debug=True)
