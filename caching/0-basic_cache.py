#!/usr/bin/env python3
'''
module that contains BasicCache
'''
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    '''basic cachign system'''
    def __init__(self) -> None:
        super().__init__()

    def put(self, key, item):
        '''put method of cache'''
        if(not key or not item):
            return
        self.cache_data[key] = item

    def get(self, key):
        '''get method of cache'''
        if(not key):
            return
        try:
            return self.cache_data.get(key)
        except KeyError:
            return None
