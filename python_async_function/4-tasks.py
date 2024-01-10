#!/usr/bin/env python3
'''
use task_wait_n with tasks
'''

from typing import List

import asyncio


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''execute max_delay n times'''
    r = []
    tasks = [task_wait_random(max_delay) for x in range(n)]
    for t in asyncio.as_completed(tasks):
        r.append(await t)
    r.sort()
    return r
