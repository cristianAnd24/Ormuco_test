# Ormuco_test

A collection of utility functions designed to aid developers in various tasks such as line overlap checking, version comparison, and a Least Recently Used (LRU) cache implementation with expiration.

## Usage
### Line Overlap Checker
Located in A.py, the function lines_overlap determines if two 1D lines overlap.

Example
'''
from A import lines_overlap

print(lines_overlap((1,5), (2,6)))  # True
print(lines_overlap((1,5), (6,8)))  # False
'''
### Version Comparison
Located in B.py, the function compare_versions compares two version strings.

Example
'''
from B import compare_versions

print(compare_versions("1.0", "1.0.1"))  # -1
print(compare_versions("1.2.3", "1.2.2"))  # 1
'''
### LRU Cache with Expiration
Located in C.py, the LRUCache class provides a least recently used cache implementation with a time-based expiration feature.

Example
'''
from C import LRUCache

cache = LRUCache(2, 5)  # Capacity of 2 items, 5 seconds expiration

cache.put(1, 1)
print(cache.get(1))  # 1
'''
## Testing
Each module comes with its tests:

'A.py' has inline testing.
'B.py' has a test function that you can run to ensure the version comparison logic works correctly.
'C.py' uses the unittest framework for its testing. Simply run C.py to execute the tests.
