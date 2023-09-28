import unittest
from kth_largest_element import find_kth_largest

def test_find_kth_largest(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        k = 1
        result, position = find_kth_largest(arr, k)
        self.assertEqual(result, 9)
        self.assertEqual(position, 5)

if __name__ == '__main__':
    unittest.main()