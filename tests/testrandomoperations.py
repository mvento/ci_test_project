from unittest import TestCase

import pandas as pd

import random_operations


class TestRandomOperations(TestCase):
    def test_float_sum(self):
        expected_result = 6
        result = random_operations.float_sum(1, 5)

        self.assertEqual(expected_result, result, 'The float_sum result didnt match')

    def test_sum_columns(self):
        data = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4], 'col3': [5, 6]})

        result_expected = pd.Series({'col1': 3, 'col2': 7, 'col3': 11})

        result = random_operations.sum_columns(data)

        self.assertTrue(result.equals(result_expected))

    def test_error(self):
        self.assertTrue(False)
