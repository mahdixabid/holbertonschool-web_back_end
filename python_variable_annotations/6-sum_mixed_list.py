#!/usr/bin/env python3
"""_summary_
sums a list of ints and floats
"""


from typing import Union, List
from math import fsum


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''return fsum(mxd_lst)'''
    return fsum(mxd_lst)
