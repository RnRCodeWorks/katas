import unittest
from cyphers.mirror_cypher import mirror

class MirrorCypherTestCase(unittest.TestCase):
    def test_simple_mirror(self):
        self.assertEqual('zyx', mirror('abc'))
    def test_blank_seed_mirror(self):
        self.assertEqual('abc', mirror('abc', ''))
    def test_simple_seed_mirror(self):
        self.assertEqual( 'wqp', mirror('abc', 'abcpqw'))
    def test_decode_mirror(self):
        self.assertEqual( 'dvoxlnv', mirror('Welcome'))
    def test_decode_outlyers_mirror(self):
        self.assertEqual( '?d!v@o[x)lnv', mirror('?W!e@l[c)ome'))
    def test_space_mirror(self):
        self.assertEqual( 'gsrh hslfow dlip', mirror('This should work'))
    def test_space_seed_mirror(self):
        self.assertEqual( 'sk shkulq thps', mirror('So should this', 'rdiokpqe'))

