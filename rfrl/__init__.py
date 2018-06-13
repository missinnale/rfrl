from flask import flask
from . import routes, api

def create_app():
    app = Flask(__name__)

    app.register_blueprint(routes.bp)
    app.register_blueprint(api.bp)

    return app