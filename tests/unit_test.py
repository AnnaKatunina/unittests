import unittest
from anagram.anagrams import reversed_words


class TestAnagrams(unittest.TestCase):

    def test_anagrams_typical(self):
        self.assertEqual(reversed_words('abcd efgh'), 'dcba hgfe')
        self.assertEqual(reversed_words('a1bcd efg!h'), 'd1cba hgf!e')
        self.assertEqual(reversed_words('11!1 1234'), '11!1 1234')
        self.assertEqual(reversed_words(''), '')

    def test_anagrams_atypical(self):
        self.assertRaises(TypeError, reversed_words, True)
        self.assertRaises(TypeError, reversed_words, 1234)
        self.assertRaises(TypeError, reversed_words, 1.5)
        self.assertRaises(TypeError, reversed_words, [1, 2])


if __name__ == '__main__':
    unittest.main()
