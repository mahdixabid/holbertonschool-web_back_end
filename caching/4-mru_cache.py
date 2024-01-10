#!/usr/bin/env python3
'''
module with most frequently  used cache
'''
from collections import OrderedDict

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    '''Most recently used'''

    def __init__(self) -> None:
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item) -> None:
        '''put with mru method'''
        if(not key or not item):
            return
        self.cache_data[key] = item
        if(len(self.cache_data.keys()) > BaseCaching.MAX_ITEMS):
            k = self.cache_data.popitem(last=False)[0]
            print('DISCARD: {}'.format(k))
            self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        '''get method WITH OrderedDict MECHANIC'''
        if (not key):
            return
        try:
            r = self.cache_data.get(key)
            self.cache_data.move_to_end(key, last=False)
            return r
        except Exception:
            return
