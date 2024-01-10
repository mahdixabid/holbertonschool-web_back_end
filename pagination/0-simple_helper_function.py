#!/usr/bin/env python3
'''helper function module'''

# from typing import Tuple


def index_range(page: int, page_size: int) -> tuple:
    '''helper function that shows ranges to be used'''
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
