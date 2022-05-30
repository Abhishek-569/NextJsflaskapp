from flask import Flask
from flask_cors import CORS

app = Flask(__name__, static_url_path='/', static_folder='./frontend/out')
CORS(app, supports_credentials=True)


@app.route("/")
def index():
    return app.send_static_file('index.html')


@app.errorhandler(404)
def not_found(err):
    return app.send_static_file('404.html')
