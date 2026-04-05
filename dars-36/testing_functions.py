import unittest
from dars_36_functions import max_num, uppercase_latter, get_evens, is_num_fib


class TestCases(unittest.TestCase):
    #task1 check    
    def test_max_3nums(self):
        answer = max(12, 7, 19)
        self.assertEqual(max_num(12, 7, 19), answer)
        
    #task2 check
    
    def test_letter(self):
        cities = ['toshkent', 'samarqand', 'farg\'ona', 'buxoro']
        self.assertEqual(uppercase_latter(cities), ['Toshkent', 'Samarqand', 'Farg\'ona', 'Buxoro'] )
    
    #task3 check
    def test_even_nums(self):
        num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(get_evens(num_list), [2, 4, 6, 8, 10])
        
    #task4 check
    def test_is_num_fib(self):
        self.assertTrue(is_num_fib(5))
        
unittest.main()