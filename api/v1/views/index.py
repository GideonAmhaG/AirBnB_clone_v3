#!/usr/bin/python3
"""module for index"""
from api.v1.views import app_views
from flask import jsonify, request

@app_views.route('/status', strict_slashes=False)
def hbnbStatus():
    """returns a JSON: "status": OK"""
    return jsonify({"status": "OK"})
