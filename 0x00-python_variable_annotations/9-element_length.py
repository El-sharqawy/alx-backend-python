#!/usr/bin/env python3
"""Length of Element"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns the length of element"""
    return [(i, len(i)) for i in lst]
