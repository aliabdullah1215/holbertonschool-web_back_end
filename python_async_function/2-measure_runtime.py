#!/usr/bin/env python3
"""
Module that measures the runtime of executing multiple asynchronous coroutines.
"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n and returns the average time.
    """
    start_time: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time: float = time.time()

    return (end_time - start_time) / n
