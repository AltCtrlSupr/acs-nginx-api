from main import app
from database import mongo

if __name__ == '__main__':
    app.config.from_object('config.Testing')
    mongo.init_app(app) # initialize here!
    app.run(debug=True)
