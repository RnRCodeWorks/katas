import unittest
from ..atbash import atbash_cypher

class AtbashTestCase(unittest.TestCase):
    def test_encode_string(self):
        self.assertEqual(atbash_cypher('This is encoded'), 'Gsrh rh vmxlwvw')
    def test_decode_string(self):
        self.assertEqual(atbash_cypher("R slkv mlylwb wvxlwvh gsrh nvhhztv"), 'I hope nobody decodes this message')


