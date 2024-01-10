#!/usr/bin/env python3
""" Session Exp Auth """
from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta
from os import getenv


class SessionExpAuth(SessionAuth):
    """ Session Exp Auth class """
    def __init__(self):
        """ init """
        try:
            self.session_duration = int(getenv('SESSION_DURATION'))
        except Exception:
            self.session_duration = 0
        self.user_id_by_session_id = dict()

    def create_session(self, user_id: str = None) -> str:
        """ creates a Session ID for a user_id """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        user_id = self.user_id_by_session_id[session_id]
        session_dictionary = {
            'user_id': user_id,
            'created_at': datetime.now()
        }
        self.user_id_by_session_id[session_id] = session_dictionary
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ returns a User ID based on a Session ID """
        session_dictionary = super().user_id_for_session_id(session_id)
        if session_dictionary is None:
            return None
        if self.session_duration <= 0:
            return session_dictionary.get('user_id')
        if 'created_at' not in session_dictionary:
            return None
        created_at = session_dictionary.get('created_at')
        if type(created_at) is not datetime:
            return None
        if (created_at + timedelta(seconds=self.session_duration) <
                datetime.now()):
            return None
        return session_dictionary.get('user_id')