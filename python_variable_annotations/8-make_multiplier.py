#!/usr/bin/env python3
"""This module provides a function that creates a multiplier function."""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by a given multiplier."""
    def multiply(n: float) -> float:
        """Multiplies a float by the predefined multiplier."""
        return n * multiplier
    return multiply
