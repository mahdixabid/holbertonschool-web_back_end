#!/usr/bin/env python3
'''
measure performance of asynchronous exec
'''

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''measure time with time.perf_counter'''
    t_time = 0.0
    s_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    t_time = time.perf_counter() - s_time
    return t_time / n
