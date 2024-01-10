#!/usr/bin/env python3
'''
await gather for parallel exec
'''
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''measure async performance'''
    st = time.perf_counter()
    coros = [async_comprehension() for i in range(4)]
    await asyncio.gather(*coros)
    return time.perf_counter() - st
