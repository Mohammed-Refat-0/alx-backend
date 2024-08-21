#!/usr/bin/python3
""" FIFOCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache cacheing class"""

    def __init__(self):
        """Initialize"""
        super().__init__()

    def put(self, key, item):
        """"assign to the dictionary 'cache_data' the item value for the key,
        using FIFO caching"""
        if key is None or item is None:
            return
        if self.cache_data > BaseCaching.MAX_ITEMS:
            self.cache_data.pop(0)
            print("DISCARD: {}".format(key))
        self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        return self.cache_data.get(key, None)
