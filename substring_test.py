'''
Unit Test for substring module
'''

import unittest
from substring import largest_substring

class substring_tests(unittest.TestCase):
    def test_one(self):
        s = 'abcdeabcdabcdefabc'
        s_answer = 'abcdef'
        self.assertEqual(largest_substring(s), s_answer)
        
    def test_two(self):
        s = 'abcabcbb'
        s_answer = 'abc'
        self.assertEqual(largest_substring(s), s_answer)
        
    def test_three(self):
        s = 'bbbbb'
        s_answer = 'b'
        self.assertEqual(largest_substring(s), s_answer)
    
    def test_four(self):
        s = 'pwwkew'
        s_answer = 'wke'
        self.assertEqual(largest_substring(s), s_answer)        
    
if __name__ == '__main__':
    unittest.main()
