#!/usr/bin/env python3
"""_summary_
insert right annotations
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''return tuple containing many elements'''
    return [(i, len(i)) for i in lst]
