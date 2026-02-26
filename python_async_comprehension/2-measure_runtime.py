#!/usr/bin/env python3
"""
Module for Task 2: Run time for four parallel comprehensions
Measures the total execution time of running four async comprehensions.
"""

import asyncio
import time

# استيراد الدالة من الملف السابق
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel using asyncio.gather.
    Measures and returns the total runtime.
    """
    start_time = time.perf_counter()

    # تشغيل 4 مهام في وقت واحد
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)

    end_time = time.perf_counter()
    return end_time - start_time
