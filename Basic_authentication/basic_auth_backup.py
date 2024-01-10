#!/usr/bin/env python3

from api.v1.auth.auth import Auth
from flask import request
from typing import List, TypeVar
import base64,  binascii
from models.user import User
from models.base import Base


class BasicAuth(Auth):
    '''Basic auth class'''
    def __init__(self):
        '''empty for now'''
        super().__init__()
    
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        '''Base64 authorization value'''
        if authorization_header is None:
            return
        if not isinstance(authorization_header, str):
            return
        auth = auth= authorization_header.split(' ')
        if auth[0] != 'Basic':
            return None

        return auth[1]
    
    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        '''decode base64 auth  header value'''
        if base64_authorization_header is None:
            return
        if not isinstance(base64_authorization_header, str):
            return
        try:
            decoded = base64.b64decode(base64_authorization_header)
        except binascii.Error as e:
            return
        return decoded.decode('utf-8')
    
    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        '''get user creds namely email and passwd'''
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        credentials = decoded_base64_authorization_header.split(':')
        if len(credentials) == 1:
            return None, None
        return credentials[0], credentials[1]
    
    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        '''return user instance'''
        if user_email is None:
            return
        if user_pwd is None:
            return
        user = User()
        