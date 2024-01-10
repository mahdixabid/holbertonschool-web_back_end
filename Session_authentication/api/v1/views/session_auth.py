#!/usr/bin/env python3
'''
module for different views
'''

import os

from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import *
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """
    handle all logins in this api
    """
    email = request.form.get('email')
    if not email:
        return jsonify({"error": "email missing"}), 400
    password = request.form.get('password')
    if not password:
        return jsonify({"error": "password missing"}), 400

    try:
        found_users = User.search({'email': email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404

    if not found_users:
        return jsonify({"error": "no user found for this email"}), 404

    for user in found_users:
        if not user.is_valid_password(password):
            print("password")
            return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    
    new_session = auth.create_session(user.id)
    user = user.to_json()
    user["email"] = email
    SESSION_NAME = os.getenv("SESSION_NAME")
    response = jsonify(user)
    response.set_cookie(SESSION_NAME, new_session)
    return response


@app_views.route('/api/v1/auth_session/logout', methods=["DELETE"],
                 strict_slashes=False)
def logout():
    '''delete session attached to request'''
    from api.v1.app import auth
    destroyed_sess = auth.destory_session(request)
    if destroyed_sess:
        return jsonify({}), 200
    return False, abort(404)
