import unittest
from hash_quad import *

class TestList(unittest.TestCase):

    def test_01a(self):
        '''test for tables size'''
        ht = HashTable(7)
        self.assertEqual(ht.get_table_size(), 7)

    def test_01b(self):
        '''test for number of entries'''
        ht = HashTable(7)
        self.assertEqual(ht.get_num_items(), 0)

    def test_01c(self):
        '''test for load factor'''
        ht = HashTable(7)
        self.assertAlmostEqual(ht.get_load_factor(), 0)

    def test_01d(self):
        '''test for creating a list with no inserts'''
        ht = HashTable(7)
        self.assertEqual(ht.get_all_keys(), [])

    def test_01e(self):
        '''test to see if a key is not in the table'''
        ht = HashTable(7)
        self.assertEqual(ht.in_table("cat"), False)

    def test_01f(self):
        '''test to see if a key has a value'''
        ht = HashTable(7)
        self.assertEqual(ht.get_value("cat"), None)

    def test_01g(self):
        '''test for index of provided key'''
        ht = HashTable(7)
        self.assertEqual(ht.get_index("cat"), None)

    def test_01h(self):
        '''test for horner hash value'''
        ht = HashTable(7)
        self.assertEqual(ht.horner_hash("cat"), 3)

    def test_02a(self):
        '''test for table size with one entry'''
        ht = HashTable(7)
        ht.insert("cat", [5])
        self.assertEqual(ht.get_table_size(), 7)

    def test_02b(self):
        '''test for number of entries'''
        ht = HashTable(7)
        ht.insert("cat", [5])
        self.assertEqual(ht.get_num_items(), 1)

    def test_02c(self):
        '''test for a load factor of one entry'''
        ht = HashTable(7)
        ht.insert("cat", [5])
        self.assertAlmostEqual(ht.get_load_factor(), 1/7)

    def test_02d(self):
        '''test for a list for one entry'''
        ht = HashTable(7)
        ht.insert("cat", [5])
        self.assertEqual(ht.get_all_keys(), ["cat"])

    def test_02e(self):
        '''test if an entry exists within the table'''
        ht = HashTable(7)
        ht.insert("cat", [5])
        self.assertEqual(ht.in_table("cat"), True)

    def test_02f(self):
        '''test for the value of a key in the table'''
        ht = HashTable(7)
        ht.insert("cat", [5])
        self.assertEqual(ht.get_value("cat"), [5])

    def test_02g(self):
        '''test for the index of the key'''
        ht = HashTable(7)
        ht.insert("cat", [5])
        self.assertEqual(ht.get_index("cat"), 3)

    def test_03(self):
        '''tests for the change in value for duplicate keys'''
        ht = HashTable(7)
        ht.insert("cat", [5])
        ht.insert("cat", [5, 17])
        self.assertEqual(ht.get_value("cat"), [5, 17])

    def test_04(self):
        '''tests for a mix of all the functions'''
        ht = HashTable(7)
        ht.insert("cat", [5])
        self.assertEqual(ht.get_index("cat"), 3)

        ht.insert("dog", [8])
        self.assertEqual(ht.get_num_items(), 2)
        self.assertEqual(ht.get_index("dog"), 6)
        self.assertAlmostEqual(ht.get_load_factor(), 2 / 7)

        ht.insert("mouse", [10])
        self.assertEqual(ht.get_num_items(), 3)
        self.assertEqual(ht.get_index("mouse"), 4)
        self.assertAlmostEqual(ht.get_load_factor(), 3 / 7)

        ht.insert("elephant", [12]) # hash table should be resized
        self.assertEqual(ht.get_num_items(), 4)
        self.assertEqual(ht.get_table_size(), 15)
        self.assertAlmostEqual(ht.get_load_factor(), 4 / 15)
        self.assertEqual(ht.get_index("cat"), 12)
        self.assertEqual(ht.get_index("dog"), 14)
        self.assertEqual(ht.get_index("mouse"), 13)
        self.assertEqual(ht.get_index("elephant"), 9)
        keys = ht.get_all_keys()
        keys.sort()
        self.assertEqual(keys, ["cat", "dog", "elephant", "mouse"])

    def test_get_tuple(self):
        '''test for attaining tuple values'''
        hsh = HashTable(1)
        hsh.insert('January', 1)
        self.assertEqual(hsh.get_tuple(), [('January', [1])])

    def test_get_value_helper(self):
        '''test for the last value'''
        hsh = HashTable(1)
        lst = [[1], [2]]
        self.assertEqual(hsh.get_value_helper(lst), [2])

    def test_mix(self):
        '''test for all functions on one case'''
        hsh = HashTable(1)
        hsh.insert('January', 1)
        self.assertEqual(hsh.get_num_items(), 1)
        self.assertEqual(hsh.get_table_size(), 3)
        self.assertAlmostEqual(hsh.get_load_factor(), 1 / 3)
        self.assertEqual(hsh.get_index("January"), 1)
        self.assertEqual(hsh.get_all_keys(), ['January'])

if __name__ == '__main__':
   unittest.main()
