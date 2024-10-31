#!/usr/bin/env python3
"""
This is a module that defines a class LIFOCache that
inherits from BaseCaching and is a caching system
"""
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """
    This is a class the inherits from BaseCachin and is a
    chaching system
    """

    def __init__(self):
        """
        Initialize the LIFOCache class and its super class
        """
        super().__init__()

    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data the
        item value for the key
        If key or item is None, this method should not do anything
        """
        if (key is None) or (item is None):
            pass
        else:
            if (len(self.cache_data) >= BaseCaching.MAX_ITEMS) and \
                            (key not in self.cache_data.keys()):
                discard_tuple = self.cache_data.popitem()
                discard_key = discard_tuple[0]
                print(f"DISCARD: {discard_key}")
                self.cache_data[key] = item
            else:
                self.cache_data[key] = item

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in
        self.cache_data, return None
        """
        if (key is None) or (key not in self.cache_data.keys()):
            return None

        return self.cache_data.get(key)
