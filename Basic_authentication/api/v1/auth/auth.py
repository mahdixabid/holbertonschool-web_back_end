#!/usr/bin/env python3

'''
Moduel for base class of Auth
'''
from flask import request
from typing import List, TypeVar


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
        if not path:
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
