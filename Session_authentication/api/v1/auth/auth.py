#!/usr/bin/env python3
'''
auth original class
'''
from flask import request
from typing import List, TypeVar
import os


class Auth():
    '''auth class for flask app'''

    def __init__(self):
        '''init'''
        pass

    # @staticmethod cause an error of missing argument for me
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''paths that  don't need errorhandling'''
        if not excluded_paths:
            return True
        if path[-1] != '/':
            path += '/'
        if path not in excluded_paths:
            return True
        return False

    def authorization_header(self, request=None) -> str:
        '''check authorization header'''
        if request is None:
            return None
        if "Authorization" not in request.headers:
            return
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        '''check if current user is ...'''
        return

    def session_cookie(self, request=None):
        '''return cookie from request'''
        if not request:
            return None
        my_session_id = os.getenv('SESSION_NAME')
        my_session_id = request.cookies.get(my_session_id)
        return my_session_id
