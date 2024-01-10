#!/usr/bin/env python3
'''
import wait_random from previous module
'''

from typing import List

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''execute max_delay n times'''
    itr = [wait_random(max_delay) for x in range(n)]
    d = []
    for i in asyncio.as_completed(itr):
        r = await i
        d.append(r)
    return(d)
