#!/usr/bin/env python3
"""This module provides a function that returns a key and the square of a value."""

from typing import Tuple, Union

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple with a string and the square of a number as a float."""
    return (k, float(v ** 2))
