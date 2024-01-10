#!/usr/bin/env python3


from flask import Flask, jsonify, request, abort, redirect, make_response
from auth import Auth
from sqlalchemy.orm.exc import NoResultFound


app = Flask(__name__)
Auth = Auth()


@app.route("/", methods=["GET"])
def get():
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=['POST'], strict_slashes=False)
def users():
    '''get user credentials'''
    email = request.form['email']
    password = request.form['password']
    try:
        Auth.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

    return jsonify({"email": email,
                    "message": "user created"})


@app.route("/sessions", methods=['POST'], strict_slashes=False)
def login() -> str:
    '''log in function'''
    email = request.form.get('email')
    password = request.form.get('password')

    if Auth.valid_login(email, password):
        sess = Auth.create_session(email)
        resp = make_response({"email": email, "message": "logged in"})
        resp.set_cookie('session_id', sess)
        return resp

    abort(401)


@app.route("/sessions", methods=['DELETE'])
def logout() -> None:
    '''logout view'''
    session = request.cookies.get('session_id')
    try:
        user = Auth.get_user_from_session_id(session_id=session)
    except NoResultFound:
        abort(403)
    if user:
        Auth.destroy_session(user.id)
        return redirect('/')


@app.route("/profile", methods=['GET'], strict_slashes=False)
def profile():
    '''return user's email'''
    session = request.cookies.get('session_id')
    try:
        user = Auth.get_user_from_session_id(session_id=session)
    except NoResultFound:
        abort(403)
    if user:
        return jsonify({"email": user.email}), 200
    abort(403)


@app.route("/reset_password", methods=['POST'], strict_slashes=False)
def get_reset_password_token():
    '''get reset token from auth module'''
    email = request.form['email']
    try:
        user = Auth._db.find_user_by(email=email)
    except NoResultFound:
        abort(403)
    new_token = Auth.get_reset_password_token(email=email)

    return jsonify({"email": email, "reset_token": new_token})


@app.route("/reset_password", methods=['PUT'], strict_slashes=False)
def update_password():
    '''update the password with token'''
    email = request.form['email']
    reset_token = request.form['reset_token']
    new_password = request.form['new_password']
    user = Auth._db.find_user_by(email=email)
    if user:
        Auth.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"}), 200

    abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
