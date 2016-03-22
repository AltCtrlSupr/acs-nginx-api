from main import app

if __name__ == '__main__':
    app.config.from_object('config.Testing')
    app.run(debug=True)
