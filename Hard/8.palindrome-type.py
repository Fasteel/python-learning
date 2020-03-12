# https://edabit.com/challenge/QuxCNBLcGJReCawjz

import unittest


def flip_array(array):
    return array[::-1]


def to_array(value):
    return list(value)


def is_decimal_palindrome(value):
    str_array = to_array(str(value))
    return str_array == flip_array(str_array)


def int_to_binary(value):
    return "{0:b}".format(value)


def is_binary_palindrome(value):
    binary_value = int_to_binary(value)
    str_array = to_array(str(binary_value))
    return str_array == flip_array(str_array)


class PalindromeType(unittest.TestCase):

    def main(self, value):
        has_binary_palindrome = is_binary_palindrome(value)
        has_decimal_palindrome = is_decimal_palindrome(value)

        if has_binary_palindrome and has_decimal_palindrome:
            return "Decimal and binary."
        if has_binary_palindrome:
            return "Binary only."
        if has_decimal_palindrome:
            return "Decimal only."

        return "Neither!"

    def test(self):
        self.assertEqual(self.main(1934391), "Decimal and binary.")
        self.assertEqual(self.main(9994521), "Binary only.")
        self.assertEqual(self.main(5841485), "Decimal and binary.")
        self.assertEqual(self.main(8337738), "Neither!")
        self.assertEqual(self.main(7447), "Decimal and binary.")
        self.assertEqual(self.main(18985), "Binary only.")
        self.assertEqual(self.main(7), "Decimal and binary.")
        self.assertEqual(self.main(1306031), "Decimal only.")
        self.assertEqual(self.main(1), "Decimal and binary.")
        self.assertEqual(self.main(1903127), "Binary only.")
        self.assertEqual(self.main(4), "Decimal only.")
        self.assertEqual(self.main(48084), "Decimal only.")
        self.assertEqual(self.main(427787), "Binary only.")
        self.assertEqual(self.main(456), "Neither!")
        self.assertEqual(self.main(313), "Decimal and binary.")
        self.assertEqual(self.main(3664663), "Decimal only.")
        self.assertEqual(self.main(585585), "Decimal and binary.")
        self.assertEqual(self.main(14441), "Decimal only.")
        self.assertEqual(self.main(8494948), "Decimal only.")
        self.assertEqual(self.main(932), "Neither!")
        self.assertEqual(self.main(7115931), "Binary only.")
        self.assertEqual(self.main(101), "Decimal only.")
        self.assertEqual(self.main(6286333), "Binary only.")


if __name__ == '__main__':
    unittest.main()
