# https://edabit.com/challenge/JzBLDzrcGCzDjkk5n

import unittest


class Karaca(unittest.TestCase):

    def get(self, val):
        val = list(val)
        reversed_val = ""
        mapping_chart = {
            'a': '0',
            'e': '1',
            'o': '2',
            'u': '3'
        }
        for i in range(len(val), 0, -1):
            character = val[i - 1]
            if character in mapping_chart.keys():
                reversed_val += mapping_chart.get(character)
            else:
                reversed_val += character

        return reversed_val + 'aca'

    def test_get(self):
        self.assertEqual(self.get('apple'), '1lpp0aca')
        self.assertEqual(self.get('banana'), '0n0n0baca')
        self.assertEqual(self.get('karaca'), '0c0r0kaca')
        self.assertEqual(self.get('burak'), 'k0r3baca')
        self.assertEqual(self.get('alpaca'), '0c0pl0aca')


if __name__ == '__main__':
    unittest.main()
