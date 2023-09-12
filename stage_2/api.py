#!/usr/bin/python3
"""
Simple REST API Module
"""
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from models import storage
from models.users import User
from os import getenv

load_dotenv()
app = Flask(__name__)


@app.route('/api', methods=['POST'], strict_slashes=False)
def create_user():
    """ Creates a user """

    data_param = request.args.get('name')

    if not data_param:
        data = request.get_json()
    else:
        data = {}
        data['name'] = data_param

    new_user = User(**data)
    new_user.save()

    return jsonify(new_user.to_dict()), 201


@app.route('/api', methods=['GET'], strict_slashes=False)
def get_user():
    """ Returns a user's details """

    name = request.args.get('name')
    id = request.args.get('user_id')
    user = storage.get_record(name, id)

    if not user:
        return jsonify("User not found"), 404

    return jsonify(user.to_dict()), 200


@app.route('/api/<user_id>', methods=['PATCH'], strict_slashes=False)
def update_user(user_id):
    """ Updates a user's details """

    user = storage.get_record(None, user_id)
    if not user:
        return jsonify(f"Error: User {user_id} not found"), 404

    data = request.get_json()
    for attr, value in data.items():
        setattr(user, attr, value)

    user.save()

    return jsonify(user.to_dict()), 201


@app.route('/api/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """ Deletes a user's record """

    user = storage.get_record(None, user_id)
    if not user:
        return jsonify(f"Error: User {user_id} not found"), 404

    storage.delete(user)

    return jsonify(f"User {user_id} deleted from the database"), 200


if __name__ == '__main__':
    API_HOST = getenv('API_HOST')
    API_PORT = getenv('API_PORT')

    host = API_HOST if API_HOST else '0.0.0.0'
    port = API_PORT if API_PORT else 5000

    app.run(port=port, host=host, debug=True)
