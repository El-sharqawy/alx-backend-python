#!/usr/bin/env python3
"""
annotated function to_kv
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns k and multipy of v"""
    return (k, float(v * v))
