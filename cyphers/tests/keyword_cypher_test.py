import unittest
from cyphers.keyword_cypher import keyword_cypher


class KeywordCypherTestCase(unittest.TestCase):
    def test_single_word(self):
        self.assertEqual('bshhk', keyword_cypher('hello','wednesday'))  # add assertion here
    def test_multiple_words(self):
        self.assertEqual('djofd eqdvn lfdqjga', keyword_cypher('alpha bravo charlie', 'delta'))
    def test_invalid_key(self):
        self.assertEqual('Invalid translation', keyword_cypher('alpha bravo charlie', 'delta1234'))

