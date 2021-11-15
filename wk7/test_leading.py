#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import unittest
import leading

class TestLeadingSubstrings(unittest.TestCase):
    """docstring"""
    
    def test_empty_string(self):
        """docstring"""
        inputted = ''
        outputted = leading.leading_substrings(inputted)
        output_expected = ['']
        self.assertEqual(outputted, output_expected, "The string is empty")
    
    def test_single_character(self):
        """docstring"""
        inputted = 's'
        outputted = leading.leading_substrings(inputted)
        output_expected = ['s']
        self.assertEqual(outputted, output_expected, "The string has one char.")
    
    def test_multiple_characters(self):
        pass
    
    def test_(self):
        pass
    
    
if __name__ == '__main__':
    unittest.main()

