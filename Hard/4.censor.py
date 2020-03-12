# https://edabit.com/challenge/zJSF5EfPe69e9sJAc

# Create a function that takes a string txt and censors any word from
# a given list lst. The text removed must be replaced by the given character char.

import unittest


class Censor(unittest.TestCase):

    def get(self, val, items, replace_char):
        for item in items:
            word_replace = ""
            for i in range(0, len(item)):
                word_replace += replace_char
            val = val.replace(item, word_replace)

        return val

    def test_get(self):
        self.assertEqual(self.get("The cow jumped over the moon.", ["cow", "over"], "*"), "The *** jumped **** the moon.")
        self.assertEqual(self.get("How do I stop myself from using python!?", ["do", "stop", "using"], "-"), "How -- I ---- myself from ----- python!?")
        self.assertEqual(self.get("Why do my cats keep eating grass?", ["Why", "keep", "eating"], "!"), "!!! do my cats !!!! !!!!!! grass?")
        self.assertEqual(self.get("If statements are pretty fun to use.", ["statements", "pretty", "to"], "~~"), "If ~~~~~~~~~~~~~~~~~~~~ are ~~~~~~~~~~~~ fun ~~~~ use.")
        self.assertEqual(self.get("I'm dyslexic, but that deos'tn matter!", ["that", "matter!"], "?"), "I'm dyslexic, but ???? deos'tn ???????")
        self.assertEqual(self.get("I should be doing work but I am doing this instead.", ["should", "but", "this"], "*"), "I ****** be doing work *** I am doing **** instead.")


if __name__ == '__main__':
    unittest.main()
