from main import app as application
from database import mongo

application.config.from_object('config.Production')
mongo.init_app(application) # initialize here!
