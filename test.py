from main import app
from database import mongo

app.config.from_object('config.Testing')
mongo.init_app(app) # initialize here!
