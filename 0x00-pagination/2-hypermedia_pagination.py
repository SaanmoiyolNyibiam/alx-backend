#!/usr/bin/env python3
"""
This is a module that defines a class that paginates a database
"""
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    This is a function that returns the index range for
    paginating items in a page.
    """
    start = page_size * (page - 1)
    end = start + page_size
    return start, end


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns the paginated database
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data = self.dataset()

        try:
            start, end = index_range(page, page_size)
            return data[start:end]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Implement a get_hyper method that takes the same
        arguments (and defaults) as get_page
        and returns a dictionary containing the following key-value pairs:

        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer
        Make sure to reuse get_page in your implementation.

        You can use the math module if necessary.
        """

        data_list = self.get_page(page, page_size)
        data_size = len(data_list)
        page_idx = page
        data_set = data_list
        pages = math.ceil(len(self.dataset()) / page_size)

        if page_idx < pages and page_idx > 0:
            next_page_idx = page + 1
        else:
            next_page_idx = None

        if page_idx == 1:
            prev_page_idx = None
        else:
            prev_page_idx = page - 1
        return {
            'page_size': data_size,
            'page': page_idx,
            'data': data_set,
            'next_page': next_page_idx,
            'prev_page': prev_page_idx,
            'total_pages_': pages
        }
