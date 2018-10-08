import unittest
import clustering
import random_data as rd
import pandas as pd
import numpy as np
import datetime

class TestClustering(unittest.TestCase):

    def test_cluster(self):
        test_df = rd.random_int(10, 9999, 'np')
        data = clustering.cluster(test_df, 10)
        self.assertEqual(isinstance(data, pd.DataFrame), True)

if __name__ == '__main__':
    unittest.main()
