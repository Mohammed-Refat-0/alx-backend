#!/usr/bin/python3
""" FIFOCache module
"""

from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary with a FIFO
    algorithm
    """

    def __init__(self):
        """Initializes the cache
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """Retrieves an item by key
        """
        return self.cache_data.get(key, None)
