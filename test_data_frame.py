import unittest
import data_frame as pc
import pandas as pd

class TestDataFrame(unittest.TestCase):

    def test_simple_df(self):
        self.assertEqual(len(pc.simple_df(10)), 10)

    def test_simple_df_with_col(self):
        self.assertEqual(len(pc.simple_df_with_col('id', 10)), 10)

    def test_more_than_num(self):
        df = pc.simple_df_with_col("id", 10)
        self.assertEqual(len(pc.more_than_num(df, "id", 5)), 4)

    def test_less_than_num(self):
        df = pc.simple_df_with_col("id", 10)
        self.assertEqual(len(pc.less_than_num(df, "id", 5)), 5)

    def test_between_num(self):
        df = pc.simple_df_with_col("id", 10)
        self.assertEqual(len(pc.between_num(df, "id", 1, 5)), 3)

if __name__ == '__main__':
    unittest.main()
