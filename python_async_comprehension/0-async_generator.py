#!/usr/bin/env python3
'''
yields values after sleeping
'''

import asyncio
from random import uniform
from types import NoneType
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''yield numbers asynchronously'''
    for _ in range(10):
        # https://splunktool.com/why-does-asynciosleep0-make-my-code-faster
        await asyncio.sleep(1)
        yield uniform(0, 10)
