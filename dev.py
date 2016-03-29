from main import app
from mongo import mongo

if __name__ == '__main__':
    app.config.from_object('config.Development')
    # mongo.init_app(app)
    app.run(debug=True)
