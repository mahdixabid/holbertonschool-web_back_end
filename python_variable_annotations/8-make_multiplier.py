#!/usr/bin/env python3
"""_summary_
returns a function that multiplies a float by multiplier.
"""
from operator import mul
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''return callable object'''
    def f(n: float) -> float:
        return n * multiplier
    return f
