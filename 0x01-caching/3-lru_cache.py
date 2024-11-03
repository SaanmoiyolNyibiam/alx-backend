#!/usr/bin/env python3
"""
This is a module that defines a class LRUCache that
inherits from BaseCaching and is a caching system
"""
from typing import Callable
from functools import wraps
BaseCaching = __import__("base_caching").BaseCaching


def call_count(method: Callable) -> Callable:
    """
    This is a decorator
    """
    @wraps(method)
    def wrapper(self, *args):
        """
        Tracks the number of calls to a method
        """
        key = args[0]
        p_list_len = len(self.priority_list)
        if p_list_len >= self.MAX_ITEMS:
            if key in self.priority_list:
                idx = self.priority_list.index(key)
                while idx < p_list_len - 1:
                    temp = self.priority_list[idx]
                    self.priority_list[idx] = self.priority_list[idx + 1]
                    self.priority_list[idx + 1] = temp
                    idx += 1
            else:
                self.priority_list.pop(0)
                self.priority_list.append(key)
        else:
            if key in self.priority_list:
                idx = self.priority_list.index(key)
                while idx < p_list_len - 1:
                    temp = self.priority_list[idx]
                    self.priority_list[idx] = self.priority_list[idx + 1]
                    self.priority_list[idx + 1] = temp
                    idx += 1
            else:
                self.priority_list.append(key)

        return method(self, *args)
    return wrapper


class LRUCache(BaseCaching):
    """
    This is a class the inherits from BaseCachin and is a
    chaching system
    """
    priority_list = []

    def __init__(self):
        """
        Initialize the LRUCache class and its super class
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
            self.update_dict(key, item)

    def update_dict(self, key, item):
        """
        Updates the cached data
        """
        if len(self.cache_data) >= self.MAX_ITEMS:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
                self.update_p_list(key)
            else:
                discard_key = self.priority_list[0]
                self.cache_data.pop(discard_key)
                print(f"DISCARD: {discard_key}")
                self.cache_data[key] = item
                self.update_p_list(key)
        else:
            self.cache_data[key] = item
            self.update_p_list(key)

    @call_count
    def update_p_list(self, key):
        """
        Updates the priority list after the put method
        is being called, instead of before the call.
        """
        return key

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in
        self.cache_data, return None
        """
        if (key is None) or (key not in self.cache_data.keys()):
            return None
        return self.get_and_cache(key)

    @call_count
    def get_and_cache(self, key):
        """
        Helps the cache method to only cache keys only when
        the get operation is valid
        """
        return self.cache_data.get(key)
