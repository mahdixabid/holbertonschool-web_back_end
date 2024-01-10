#!/usr/bin/env python3
"""_summary_
return firs t element of a list
"""
from typing import Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''return lst[0]'''
    if lst:
        return lst[0]
    else:
        return None
