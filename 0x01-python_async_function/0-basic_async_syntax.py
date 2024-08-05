#!/usr/bin/env python3
"""Async Python Function"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """wait for random time between 0 and max_delay seconds"""
    random_num = random.uniform(0, max_delay)
    await asyncio.sleep(random_num)
    return random_num
