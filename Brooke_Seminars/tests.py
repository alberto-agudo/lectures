# Example taken from Gries et al. 2013. Practical Programming: An Introduction
# to Computer Science Using Python 3

import unittest
import tools

# Inheriting because of unittest.main()
# You should know whether you need to import a module or if it is already imported from another intermediate module.
# You will mostly use the TestCase class.
class TestRunningSum(unittest.TestCase):
    '''Tests for running_sum.'''

    def test_running_sum_empty(self):
        '''Test an empty list.'''
        inputted = []
        tools.running_sum(inputted)
        # Inputted is modified in place.
        output_expected = []
        self.assertEqual(output_expected, inputted, "The list is empty.")

    def test_running_sum_one(self):
        '''Test a one-item list.'''
        inputted = [2]
        tools.running_sum(inputted)
        output_expected = [2]
        self.assertEqual(output_expected, inputted, "The list contains one item.")

    def test_running_sum_two(self):
        '''Test a two-item list.'''
        inputted = [2, 5]
        tools.running_sum(inputted)
        output_expected = [2, 7]
        self.assertEqual(output_expected, inputted, "The list contains two items.")

    def test_running_sum_multi_neg(self):
        '''Test a list of negative values.'''
        inputted = [-1, -5, -3, -4]
        tools.running_sum(inputted)
        output_expected = [-1, -6, -9, -13]
        self.assertEqual(output_expected, inputted, "The list contains only negative values.")

    def test_running_sum_multi_zeros(self):
        '''Test a list of zeros.'''
        inputted = [0, 0, 0, 0]
        tools.running_sum(inputted)
        output_expected = [0, 0, 0, 0]
        self.assertEqual(output_expected, inputted, "Not working with zeros.")

    def test_running_sum_multi_pos(self):
        '''Test a list of positive values.'''
        inputted = [4, 2, 3, 6]
        tools.running_sum(inputted)
        output_expected = [4, 6, 9, 15]
        self.assertEqual(output_expected, inputted, "Not working with positive values.")

    def test_running_sum_multi_mix(self):
        '''Test a list of mixed values.'''
        inputted = [4, 0, 2, -5]
        tools.running_sum(inputted)
        output_expected = [4, 4, 6, 1]
        self.assertEqual(output_expected, inputted, "Not working with mixed values.")

# Run the code above.
if __name__ == '__main__':
    # Here you use a special unittest case.
    # It is a very specific way of running the script that allows you to 
    # keep on running the code while the errors are raised. 
    unittest.main()

