#!/usr/bin/env python3
"""
Module that provides a helper function for pagination.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple containing the start and end index
    corresponding to the range of indexes for pagination.
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
