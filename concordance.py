from hash_quad import *
import string

class Concordance:

    def __init__(self):
        self.stop_table = None          # hash table for stop words
        self.concordance_table = None   # hash table for concordance

    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        # file -> list
        self.stop_table = HashTable(191)
        try:
            file = open(filename, 'r')
            for i in file:
                stop_words = i.strip()
                self.stop_table.insert(stop_words, 0)
            file.close()
        except FileNotFoundError:
            raise FileNotFoundError

    def load_concordance_table(self, filename):
        """ Read words from input text file (filename) and insert them into the concordance hash table, 
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
        Starting size of hash table should be 191: self.concordance_table = HashTable(191)
        Process of adding new line numbers for a word (key) in the concordance:
            If word is in table, get current value (list of line numbers), append new line number, insert (key, value)
            If word is not in table, insert (key, value), where value is a Python List with the line number
        If file does not exist, raise FileNotFoundError"""
        # file -> list
        self.concordance_table = HashTable(191)
        try:
            file = open(filename, 'r')
            stop_table_list = self.stop_table.get_all_keys()
            count = 0
            punc = string.punctuation
            num = string.digits
            exclude = punc + num
            for line in file:
                count += 1
                for chara in exclude:
                    if chara == "'":
                        line = line.replace(chara, '')
                    else:
                        line = line.replace(chara, ' ')
                files = line.split()
                words = []
                for word in files:
                    word = word.lower()
                    words.append(word)
                for i in words:
                    if i not in stop_table_list:
                        self.concordance_table.insert(i, count)
            file.close()
        except FileNotFoundError:
            raise FileNotFoundError

    def write_concordance(self, filename):
        """ Write the concordance entries to the output file(filename)
        See sample output files for format."""
        # list -> file
        output = open(filename, 'w')
        key_lst = self.concordance_table.get_tuple()
        key_lst.sort()
        for i in key_lst:
            string_val = ''
            if i != key_lst[0]:
                output.write("\n")
            for val in (i[1]):
                string_val = string_val + " " + str(val)
            output.write(i[0] + ":" + string_val)
        output.close()

if __name__ == '__main__':
    # conc = Concordance()
    # conc.load_stop_table("stop_words.txt")
    # conc.load_concordance_table("file1.txt")
    # conc.write_concordance("file1_con.txt")
    # conc = Concordance()
    # conc.load_stop_table("stop_words.txt")
    # conc.load_concordance_table("file2.txt")
    # conc.write_concordance("file2_con.txt")
    conc = Concordance()
    conc.load_stop_table("stop_words.txt")
    conc.load_concordance_table("declaration.txt")
    conc.write_concordance("declaration_con.txt")