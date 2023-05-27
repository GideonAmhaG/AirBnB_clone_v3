#!/usr/bin/python3
"""module for api"""
from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify
from models import storage


if __name__ == "__main__":
    pass


hbnb_models = {
	"Amenity": "amenities",
	"City": "cities",
	"Place": "places",
	"Review": "reviews",
	"State": "states",
	"User": "users"
}

@app_views.route('/status', strict_slashes=False)
def hbnbStatus():
    """returns a JSON: "status": OK"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def hbnbStats():
    """Create an endpoint that retrieves the number of each objects by type"""
    return_dict = {}
    for key, value in hbnb_models.items():
        return_dict[key] = storage.count(value)
    return jsonify(return_dict)
