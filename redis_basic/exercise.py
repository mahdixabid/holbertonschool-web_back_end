#!/usr/bin/env python3
"""module for redis cache"""


import uuid
from functools import wraps
from typing import Callable, Optional, Union
import redis


def call_history(method: Callable) -> Callable:
    """wrapper function for any metjod that stores io"""
    @wraps(method)
    def save_io(self, *args):
        """save input and ouput of a method in redis cache"""
        inputs = str(args)
        self._redis.rpush(f'{method.__qualname__}:inputs', inputs)
        outputs = method(self, inputs)
        self._redis.rpush(f'{method.__qualname__}:outputs', outputs)
        return outputs
    return save_io


def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """increment counter for calling funciton in redis cache"""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def replay(fn: Callable) -> None:
    """display calls of a particular function"""
    cache = redis.Redis()
    count = cache.llen(f'{fn.__qualname__}:inputs')
    print('{:} was called {:} times:'.format(fn.__qualname__, count))
    inputs = cache.lrange(f'{fn.__qualname__}:inputs', 0, -1)
    outputs = cache.lrange(f'{fn.__qualname__}:outputs', 0, -1)
    for i, o in zip(inputs, outputs):
        print('{:}(*{:}) -> {:}'.format(fn.__qualname__,
                                        i.decode(), o.decode()))


class Cache():
    """cache that is linked to a db"""

    def __init__(self) -> None:
        """init redis cache"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data:
              Union[str, bytes, int, float]) -> str:
        """store random key in db"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None):
        """documentation for get funcion that uses conversion"""
        if not fn:
            value = self._redis.get(key)
        else:
            value = self._redis.get(key)
            # while testing in the ipython cli this seems to work
            value = fn(value)
        return value

    def get_str(self, key):
        """call get with str function"""
        return self.get(key, str)

    def get_int(self, key):
        """exec get with int conversion"""
        value = self.get(key)
        try:
            value = int(value)
        except Exception:
            return
