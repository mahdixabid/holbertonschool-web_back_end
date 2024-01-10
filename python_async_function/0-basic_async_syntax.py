#!/usr/bin/env python3
'''
asynchronous coroutine that takes in an integer argument
named wait_random that waits for a random delay between 0
and max_delay
'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''wait for max_delay and return and return it'''
    v = random.uniform(0, max_delay)
    await asyncio.sleep(v)
    return(v)
