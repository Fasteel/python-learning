# https://edabit.com/challenge/G9QRtAGXb9Cu368Pw

# Create a function that takes a variable number of groups of items,
# and returns the number of ways the items can be arranged, with one
# item from each group. Order does not matter.

import unittest


class Combinations(unittest.TestCase):

    def combinations(self, *args):
        if len(args) == 0:
            return 0

        val = 1
        for arg in args:
            if arg == 0:
                continue

            val *= arg

        return val

    def test_combinations(self):
        self.assertEqual(self.combinations(2), 2)
        self.assertEqual(self.combinations(2), 2)
        self.assertEqual(self.combinations(2, 3), 6)
        self.assertEqual(self.combinations(3, 5), 15)
        self.assertEqual(self.combinations(5, 6, 7), 210)
        self.assertEqual(self.combinations(5, 5, 5, 5), 625)
        self.assertEqual(self.combinations(3, 6, 9), 162)
        self.assertEqual(self.combinations(2, 3, 4, 5, 6, 7, 8, 9, 10), 3628800)
        self.assertEqual(self.combinations(4, 5, 6), 120)
        self.assertEqual(self.combinations(5, 6, 7, 8), 1680)
        self.assertEqual(self.combinations(6, 7, 0), 42)


if __name__ == '__main__':
    unittest.main()
