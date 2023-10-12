import unittest
from eat_speed import eatingMinimumSpeed


class TestEating(unittest.TestCase):
    def test_first(self):
        piles = [3, 6, 7, 11]
        H = 8
        self.assertEqual(eatingMinimumSpeed(piles, H), 4)

    def test_second(self):
        piles = [1, 6, 2, 9]
        H = 4
        self.assertEqual(eatingMinimumSpeed(piles, H), 9)

    def test_third(self):
        piles = [6, 9, 1]
        H = 2
        self.assertEqual(eatingMinimumSpeed(piles, H), 9)


if __name__ == "__main__":
    unittest.main()
