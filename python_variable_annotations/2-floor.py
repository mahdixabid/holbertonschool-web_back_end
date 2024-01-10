#!/usr/bin/env python3
"""_summary_
contains floor function
that uses math.floor() method
"""

from math import modf


def floor(n: float) -> int:
    '''return the integer part of a flaot'''
    return int(modf(n)[1])
