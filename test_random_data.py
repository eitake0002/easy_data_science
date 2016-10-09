import unittest
import random_data as rd
import pandas as pd


class TestRandomData(unittest.TestCase):

    def test_simple_df(self):
        self.assertEqual(len(rd.generate_int(10, 9999)), 10)

if __name__ == '__main__':
    unittest.main()
