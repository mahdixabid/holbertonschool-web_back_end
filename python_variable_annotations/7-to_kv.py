#!/usr/bin/env python3
"""_summary_
	returns an annotated tuple
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
	'''returns a tuple with str ad float'''
	return (k, v**2)
