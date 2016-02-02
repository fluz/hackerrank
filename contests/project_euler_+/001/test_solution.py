import unittest
import solution

from ddt import ddt, file_data


@ddt
class TddProjectEuler001(unittest.TestCase):

    @file_data("dataset2test.json")
    def test_case(self, input, output):
        n_cases = input.pop(0)
        for i in xrange(n_cases):
            result = solution.sum_multiples_of_three_and_five(input[i])
            self.assertEqual(result, output[i])
