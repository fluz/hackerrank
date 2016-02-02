import unittest
import solution

from ddt import ddt, file_data


@ddt
class TddProjectEuler002(unittest.TestCase):

    @file_data("dataset2test.json")
    def test_case(self, input, output):
        n_cases = input.pop(0)
        for i in xrange(n_cases):
            result = solution.sum_even_fib(input[i])
            self.assertEqual(result, output[i])
