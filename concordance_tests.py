import unittest
from concordance import *

class TestList(unittest.TestCase):

    def test_01(self):
        '''test case for file1'''
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("file1.txt")
        conc.write_concordance("file1_con.txt")
        self.assertTrue(compare_files("file1_con.txt", "file1_sol.txt"))

    def test_02(self):
        '''test case for file2'''
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("file2.txt")
        conc.write_concordance("file2_con.txt")
        self.assertTrue(compare_files("file2_con.txt", "file2_sol.txt"))

    def test_03(self):
        '''test case for declaration'''
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("declaration.txt")
        conc.write_concordance("declaration_con.txt")
        self.assertTrue(compare_files("declaration_con.txt", "declaration_sol.txt"))
        self.assertFalse(compare_files("file2_con.txt", "declaration_sol.txt"))

    def test_x(self):
        '''test case for load_stop_table with an error file'''
        conc = Concordance()
        with self.assertRaises(FileNotFoundError):
            conc.load_stop_table('stopword.txt')

    def test_y(self):
        '''test case for load_concordance_table with an error file'''
        conc = Concordance()
        with self.assertRaises(FileNotFoundError):
            conc.load_concordance_table('faker.txt')



# Compare files - takes care of CR/LF, LF issues
def compare_files(file1,file2):
    match = True
    done = False
    with open(file1, "r") as f1:
        with open(file2, "r") as f2:
            while not done:
                line1 = f1.readline().strip()
                line2 = f2.readline().strip()
                if line1 == '' and line2 == '':
                    done = True
                if line1 != line2:
                    done = True
                    match = False
    return match

if __name__ == '__main__':
   unittest.main(warnings="ignore")
