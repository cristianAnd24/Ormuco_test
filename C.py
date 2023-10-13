import unittest
import time
import collections

class LRUCache:
    def __init__(self, capacity: int, expiration: int):
        self.capacity = capacity
        self.expiration = expiration
        self.cache = collections.OrderedDict()
        self.timestamps = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        # Check for expiration
        if time.time() - self.timestamps[key] > self.expiration:
            self.cache.pop(key)
            self.timestamps.pop(key)
            return -1

        # Move the accessed item to the end
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        else:
            if len(self.cache) >= self.capacity:
                # Remove oldest cache entry
                oldest = next(iter(self.cache))
                self.cache.pop(oldest)
                self.timestamps.pop(oldest)
                
        self.cache[key] = value
        self.timestamps[key] = time.time()

class TestLRUCache(unittest.TestCase):

    def setUp(self):
        self.cache = LRUCache(2, 5)  # 2 items capacity, 5 seconds expiration

    def test_basic_functionality(self):
        self.cache.put(1, 1)
        self.cache.put(2, 2)
        
        self.assertEqual(self.cache.get(1), 1)
        self.assertEqual(self.cache.get(2), 2)

        self.cache.put(3, 3)
        self.assertEqual(self.cache.get(1), -1)  # 1 should be evicted due to LRU
        self.assertEqual(self.cache.get(3), 3)

    def test_expiration(self):
        self.cache.put(1, 1)
        self.cache.put(2, 2)

        time.sleep(6)  # Sleep for 6 seconds to cause expiration

        self.assertEqual(self.cache.get(1), -1)  # Expired
        self.assertEqual(self.cache.get(2), -1)  # Expired

    def test_update_no_expiration(self):
        self.cache.put(1, 1)
        self.cache.put(2, 2)
        time.sleep(3)
        self.cache.put(1, 3)  # Updating value of key 1 resets its expiration

        time.sleep(3)
        self.assertEqual(self.cache.get(1), 3)  # Should not be expired
        self.assertEqual(self.cache.get(2), -1)  # Expired

if __name__ == '__main__':
    unittest.main()