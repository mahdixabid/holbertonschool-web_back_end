#!/usr/bin/env python3
'''
better model
'''

from models.base import Base

class UserSession(Base):
    '''better user model'''

    def __init__(self, *args: list, **kwargs: dict):
        '''constructor'''
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
        