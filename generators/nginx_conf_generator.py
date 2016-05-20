from database import mongo

from flask import render_template

class NginxConfGenerator():
    def __init__(self):
        self.mongo = mongo

    def write_file(filename, data):
        with open(filename, 'w') as wfile:
            wfile.write(data)
            wfile.close()
            return True
        return False

    def generate(self):
        resources = self.mongo.db['virtualhost'].find({})
        self.render(resources)
        return True

    def render(self, resources):
        return True
        # return render_template('nginx.conf.j2', vhosts=resources)
