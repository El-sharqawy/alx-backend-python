#!/usr/bin/env python3
"""
annotated multiplier function
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """a function that makes multiplier"""

    def func(x: float) -> float:
        return x * multiplier

    return func
