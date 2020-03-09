class HashTable:

    def __init__(self, table_size):         # can add additional attributes
        self.table_size = table_size        # initial table size
        self.hash_table = [None]*table_size # hash table
        self.num_items = 0                  # empty hash table


    def insert(self, key, value):
        """ Inserts an entry into the hash table (using Horner hash function to determine index, 
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is any object (e.g. Python List).
        If the key is not already in the table, the key is inserted along with the associated value
        If the key is is in the table, the new value replaces the existing value.
        When used with the concordance, value is a Python List of line numbers.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased (doubled + 1)."""
        # str , list -> list
        hash_val = self.horner_hash(key)
        quad = 1
        while self.hash_table[hash_val % self.table_size] is not None:
            if self.hash_table[hash_val % self.table_size][0] != key:
                hash_val += quad
                quad += 2
            else:
                break
        if self.hash_table[hash_val % self.table_size] is not None and self.hash_table[hash_val % self.table_size][0] == key:
            if self.hash_table[hash_val % self.table_size][1][len(self.hash_table[hash_val % self.table_size][1]) - 1] < value:
                self.hash_table[hash_val % self.table_size][1].append(value)
        if self.hash_table[hash_val % self.table_size] is None:
            self.hash_table[hash_val % self.table_size] = (key, [value])
            self.num_items += 1
        if self.get_load_factor() > 0.5:
            old_hash = self.hash_table
            new_size = self.table_size * 2 + 1
            new_hash = [None] * new_size
            self.table_size = new_size
            for i in old_hash:
                if i is not None:
                    hash_val = self.horner_hash(i[0])
                    quad = 1
                    while new_hash[hash_val % self.table_size] is not None:
                        hash_val += quad
                        quad += 2
                    else:
                        new_hash[hash_val % self.table_size] = i
            self.hash_table = new_hash


    def horner_hash(self, key):
        """ Compute and return an integer from 0 to the (size of the hash table) - 1
        Compute the hash value by using Horner’s rule, as described in project specification."""
        # str -> int
        h_val = 0
        n = min(8, len(key))
        for i in range(n):
            h_val += ord(key[i]) * (31 ** (n - 1 - i))
        return h_val % self.get_table_size()

    def in_table(self, key):
        """ Returns True if key is in an entry of the hash table, False otherwise. Must be O(1)."""
        # str -> bool
        value = self.get_index(key)
        if value is None:
            return False
        else:
            return True

    def get_index(self, key):
        """ Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None. Must be O(1)."""
        # str -> int
        hash_value = self.horner_hash(key)
        quad = 0
        while self.hash_table[(hash_value + quad ** 2) % (self.get_table_size())] is not None:
            if self.hash_table[(hash_value + quad ** 2) % (self.get_table_size())][0] == key:
                return (hash_value + quad ** 2) % (self.get_table_size())
            else:
                quad += 1
        else:
            return None

    def get_all_keys(self):
        """ Returns a Python list of all keys in the hash table."""
        # str -> list
        empty_list = []
        for i in self.hash_table:
            if i is not None:
                empty_list.append(i[0])
        return empty_list

    def get_value(self, key):
        """ Returns the value (for concordance, list of line numbers) associated with the key.
        If key is not in hash table, returns None. Must be O(1)."""
        # str -> list
        if not self.in_table(key):
            return None
        else:
            value = self.get_index(key)
            return self.get_value_helper(self.hash_table[value][1])

    def get_value_helper(self, lst):
        '''Returns the last value in the list'''
        # list -> list
        reverse = lst[::-1]
        return reverse[0]

    def get_num_items(self):
        """ Returns the number of entries (words) in the table. Must be O(1)."""
        # list -> int
        return self.num_items

    def get_table_size(self):
        """ Returns the size of the hash table."""
        # list -> int
        return self.table_size

    def get_load_factor(self):
        """ Returns the load factor of the hash table (entries / table_size)."""
        # int int -> float
        return self.num_items / self.table_size

    def get_tuple(self):
        '''Returns all the tuples for the hash table'''
        # list -> tuple
        list_t = []
        for i in self.hash_table:
            if i is not None:
                list_t.append(i)
        return list_t

if __name__ == '__main__':
    ht = HashTable(7)
    ht.insert("cat", [5])
    ht.get_value("cat")

