import unittest
import random_data as rd
import pandas as pd
import numpy as np
import datetime

class TestRandomData(unittest.TestCase):

    def test_random_int(self):

        data = rd.random_int(1)
        self.assertEqual(isinstance(data, np.ndarray), True)

        data = rd.random_int(1, maximum=10)
        self.assertEqual(isinstance(data, np.ndarray), True)

        data = rd.random_int(1, maximum=10, data_type='df')
        self.assertEqual(isinstance(data, pd.DataFrame), True)

        data = rd.random_int(1, maximum=10, data_type="df", cols=["col_1"])
        self.assertEqual(isinstance(data, pd.DataFrame), True)

        data = rd.random_int(1, maximum=10, data_type="np")
        self.assertEqual(isinstance(data, np.ndarray), True)

        data = rd.random_int(1, maximum=100, data_type="se")
        self.assertEqual(isinstance(data, pd.Series), True)

        data = rd.random_int(1, maximum=10, data_type="invalid")
        self.assertEqual(data[0], False)

    def test_random_str(self):
        data = rd.random_str(10)
        self.assertEqual(isinstance(data, str), True)

    def test_random_list_str(self):
        data = rd.random_list_str(10)
        self.assertEqual(isinstance(data, list), True)

    def test_random_df_str(self):
        data = rd.random_df_str(10)
        self.assertEqual(isinstance(data, pd.DataFrame), True)

    def test_random_datetime(self):
        data = rd.random_datetime()
        self.assertEqual(isinstance(data, datetime.datetime), True)

    def test_random_datetime(self):
        data = rd.random_datetime_list(10)
        self.assertEqual(isinstance(data, list), True)

    def test_random_datetime_df(self):
        data = rd.random_datetime_df(10)
        self.assertEqual(isinstance(data, pd.DataFrame), True)

    def test_df_order_datetime(self):

        data = rd.df_order_datetime(10)
        self.assertEqual(isinstance(data, pd.DataFrame), True)

        data = rd.df_order_datetime(10, "days")
        self.assertEqual(isinstance(data, pd.DataFrame), True)

        data = rd.df_order_datetime(10, "hours")
        self.assertEqual(isinstance(data, pd.DataFrame), True)

        data = rd.df_order_datetime(10, "minutes")
        self.assertEqual(isinstance(data, pd.DataFrame), True)

        data = rd.df_order_datetime(10, "seconds")
        self.assertEqual(isinstance(data, pd.DataFrame), True)

        data = rd.df_order_datetime(10, "invalid")
        self.assertEqual(isinstance(data, pd.DataFrame), False)

if __name__ == '__main__':
    unittest.main()
