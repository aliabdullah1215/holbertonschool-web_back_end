#!/usr/bin/env python3
"""
Module for Task 0: Async Generator
Contains a coroutine that loops 10 times and yields random numbers.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Loop 10 times, wait 1 second asynchronously each time,
    then yield a random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
