#!/usr/bin/env python3
'''
module that contains LIFOCache
'''

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    '''lifo cache'''
    def __init__(self) -> None:
        super().__init__()

    def put(self, key, value):
        '''put method takes key, value'''
        if(not key or not value):
            return
        if(len(self.cache_data.keys()) == BaseCaching.MAX_ITEMS):
            r = sorted(self.cache_data.keys())[-1]
            del self.cache_data[r]
            print('DISCARD: {}'.format(r))
        self.cache_data[key] = value

    def get(self, key):
        '''get method'''
        if(not key):
            return
        try:
            return self.cache_data.get(key)
        except Exception:
            return
