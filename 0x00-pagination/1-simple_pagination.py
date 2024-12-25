"""
This is a module that defines a class that paginates a database
"""
import csv
from typing import List, Tuple


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
