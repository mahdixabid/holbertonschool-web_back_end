#!/usr/bin/env python3
"""
Main file
"""
from http import cookies

import requests

from app import *

local_host = 'http://192.168.1.23:5000'


def register_user(email: str, password: str) -> None:
    '''register user test'''

    with requests.session() as s:
        data = {"email": email, "password": password}
        r = requests.post('{:s}/users'.format(local_host), data=data)
        assert r.status_code == 200
        assert r.json() == {'email': email, 'message': 'user created'}


def log_in_wrong_password(email: str, password: str) -> None:
    '''log in with password not in db'''
    data = {"email": email, "password": password}
    r = requests.post('{:s}/sessions'.format(local_host), data=data)

    assert r.status_code == 401


def log_in(email: str, password: str) -> str:
    '''log in with valid credentials'''

    with requests.session() as s:
        data = {"email": email, "password": password}
        r = requests.post('{:s}/sessions'.format(local_host), data=data)

        assert r.json() == {"email": email, "message": "logged in"}
        assert r.cookies is not None

        return r.cookies.get('session_id')


def profile_unlogged() -> None:
    '''log out of session'''
    with requests.session() as s:
        cookies = {"session_id": ""}
        r = requests.get('{:s}/profile'.format(local_host), cookies=cookies)

        assert r.status_code == 403


def profile_logged(session_id):
    '''check if profile is logged'''
    with requests.session() as s:
        cookies = {"session_id": session_id}
        r = requests.get('{:s}/profile'.format(local_host), cookies=cookies)

        assert r.status_code == 200


def log_out(session_id):
    '''log profile out'''
    with requests.session() as s:
        cookies = {"session_id": session_id}
        r = requests.delete('{:s}/sessions'.format(local_host),
                            cookies=cookies,
                            allow_redirects=False)  # might have to remove

        assert r.status_code == 302


def reset_password_token(email: str) -> str:
    '''get reset token'''
    data = {"email": email}

    with requests.session() as s:
        r = requests.post('{:s}/reset_password'.format(local_host), data=data)

        assert r.status_code == 200
        reset_token = r.json().get('reset_token')

        assert r.json() == {"email": email, "reset_token": reset_token}

        return reset_token


def update_password(EMAIL, reset_token, NEW_PASSWD):
    '''update password for user'''
    data = {
        "email": EMAIL,
        "reset_token": reset_token,
        "new_password": NEW_PASSWD,
    }

    with requests.session() as s:
        r = requests.put('{:s}/reset_password'.format(local_host), data=data)

        assert r.status_code == 200

        assert r.json() == {"email": EMAIL, "message": "Password updated"}


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"

if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
