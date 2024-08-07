#!/usr/bin/env python3
"""fixed to correct Duck Type"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """correct Duck"""
    if lst:
        return lst[0]
    else:
        return None
