from main import app

if __name__ == '__main__':
    app.config.from_object('config.Development')
    app.run(debug=True)
