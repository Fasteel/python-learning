# https://edabit.com/challenge/jwzAdBnJnBxCe4AXP

# Given a number, return the difference between the maximum and
# minimum numbers that can be formed when the digits are rearranged.

import unittest


class RearangedDifference(unittest.TestCase):

    def reorg(self, value, max):
        value_array = list(str(value))
        value_array.sort(reverse=max)
        return int(''.join(value_array))

    def diff(self, value):
        return self.reorg(value, True) - self.reorg(value, False)

    def test(self):
        self.assertEqual(self.diff(9092564), 9719721)
        self.assertEqual(self.diff(1308821), 8719722)
        self.assertEqual(self.diff(8386568), 5319765)
        self.assertEqual(self.diff(7794084), 9429651)
        self.assertEqual(self.diff(6366093), 9329661)
        self.assertEqual(self.diff(7863060), 8729622)
        self.assertEqual(self.diff(3368327), 6429654)
        self.assertEqual(self.diff(7218787), 7599933)
        self.assertEqual(self.diff(7723188), 7639533)
        self.assertEqual(self.diff(8816317), 7739523)
        self.assertEqual(self.diff(8824349), 7539543)
        self.assertEqual(self.diff(3320707), 7709823)
        self.assertEqual(self.diff(1695488), 8429652)
        self.assertEqual(self.diff(2120034), 4309866)
        self.assertEqual(self.diff(5300586), 8619732)
        self.assertEqual(self.diff(3538814), 7519743)
        self.assertEqual(self.diff(1336939), 8629632)
        self.assertEqual(self.diff(6290200), 9619731)
        self.assertEqual(self.diff(5268866), 6299964)
        self.assertEqual(self.diff(5155458), 7099983)


if __name__ == '__main__':
    unittest.main()
