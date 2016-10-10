import unittest
import random_data as rd
import pandas as pd
import numpy as np


class TestRandomData(unittest.TestCase):

    def test_simple_df(self):
        data = rd.rand_int(10, 10)
        self.assertEqual(isinstance(data, np.ndarray), True)

    def test_random_str(self):
        data = rd.random_str(10)
        self.assertEqual(isinstance(data, str), True)

    def test_random_list_str(self):
        data = rd.random_list_str(10)
        self.assertEqual(isinstance(data, list), True)

    def test_random_df_str(self):
        data = rd.random_df_str(10)
        self.assertEqual(isinstance(data, pd.DataFrame), True)

if __name__ == '__main__':
    unittest.main()
