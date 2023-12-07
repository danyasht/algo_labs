import unittest


def find_needle(haystack, needle):
    comparisons = 0
    last_index = -1  

    needle_length = len(needle)
    haystack_length = len(haystack)

    # Проходимо по тексту "haystack" від початку до кінця
    for i in range(haystack_length - needle_length + 1):
        match = True

        for j in range(needle_length):
            comparisons += 1
            if haystack[i + j] != needle[j]:
                match = False
                break
        
        if match:
            last_index = i

    return last_index, comparisons

class TestSubstringSearch(unittest.TestCase):
    def test_find_last_index(self):
        haystack = "This is a haystack and we're looking for a needle in this haystack needle"
        needle = "needle"
        expected_index = 67
        expected_comparisons = 80

        index, comparisons = find_needle(haystack, needle)

        self.assertEqual(index, expected_index)
        self.assertEqual(comparisons, expected_comparisons)


if __name__ == "__main__":
    unittest.main()
