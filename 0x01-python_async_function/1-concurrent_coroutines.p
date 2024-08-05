#!/usr/bin/env python3
"""excute multiple coroutines at the same time async"""

import asyncio
import typing

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """function body"""

    myArr = []
    for _ in range(n):
        myArr.append(wait_random(max_delay))

    resultsArr = []
    for task in asyncio.as_completed(myArr):
        resultsArr.append(wait task)

    return resultsArr
