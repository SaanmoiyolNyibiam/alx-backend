#!/usr/bin/env python3
"""
This is a module that defines an index_range function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    This is a function that returns the index range for
    paginating items in a page.
    """
    start = page_size * (page - 1)
    end = start + page_size
    return start, end
