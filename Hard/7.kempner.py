# https://edabit.com/challenge/qQnWXBsQaH73yY8r4

import unittest


class Kempner(unittest.TestCase):
    def facto(self, value):
        if value < 2:
            return 1
        else:
            return value * self.facto(value - 1)

    def main(self, value):
        for i in range(1, value):
            if (self.facto(i) % value) == 0:
                return i

        return value

    def test(self):
        self.assertEqual(self.main(6), 3)
        self.assertEqual(self.main(10), 5)
        self.assertEqual(self.main(2), 2)
        self.assertEqual(self.main(21), 7)
        self.assertEqual(self.main(1), 1)
        self.assertEqual(self.main(4), 4)
        self.assertEqual(self.main(13), 13)
        self.assertEqual(self.main(29), 29)
        self.assertEqual(self.main(68), 17)
        self.assertEqual(self.main(71), 71)
        self.assertEqual(self.main(100), 10)


if __name__ == '__main__':
    unittest.main()
