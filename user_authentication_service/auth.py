#!/usr/bin/env python3
'''
implement password security
'''

from uuid import uuid1
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    '''returns salted hash of password'''
    p = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return p


def _generate_uuid() -> str:
    '''generate uuid4'''
    return str(uuid1())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email=None, password=None) -> User:
        '''register user if not already registered'''
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError('User {:} already exists'.format(email))
        except NoResultFound:
            h_p = _hash_password(password)
            user = self._db.add_user(email, h_p)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        '''validate credentials'''
        if not email or not password:
            return False
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False

        return bcrypt.checkpw(password.encode('utf-8'), user.hashed_password)

    def create_session(self, email):
        '''assign zsessiohn_id to user'''
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None

        self._db.update_user(user.id, session_id=_generate_uuid())
        return user.session_id

    def get_user_from_session_id(self, session_id):
        '''get user from session id '''

        if not session_id:
            return

        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return

        return user

    def destroy_session(self, user_id):
        '''destroy session by user_id'''
        if not user_id:
            return
        try:
            user = self._db.find_user_by(id=user_id)
        except NoResultFound:
            return
        self._db.update_user(user_id=user_id, session_id=None)
        return

    def get_reset_password_token(self, email) -> str:
        '''password reset'''
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError

        _new_token = _generate_uuid()
        self._db.update_user(user.id, reset_token=_new_token)
        return _new_token

    def update_password(self, reset_token, password):
        '''update password if token is valid'''
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError

        password = _hash_password(password)

        self._db.update_user(user.id,
                             hashed_password=password, reset_token=None)

        return
