#!/usr/bin/python3
"""module for app"""
from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify, make_response
from flask_cors import CORS
from os import getenv
from models import storage


app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown(exception):
    """declare a method to handle @app.teardown_appcontext"""
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """create a handler for 404 errors that returns a JSON-formatted 404
    status code response"""
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = getenv("HBNB_API_PORT", "5000")
    app.run(host=host, port=port)
