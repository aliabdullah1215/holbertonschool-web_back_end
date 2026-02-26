#!/usr/bin/env python3
"""
Module that measures the runtime of parallel async comprehensions.
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel and measures runtime.
    """
    start_time: float = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    end_time: float = time.time()

    return end_time - start_time
