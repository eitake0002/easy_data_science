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

    def test_concat_row(self):
        df1 = pd.DataFrame([1,2,3])
        df2 = pd.DataFrame([4,5,6])
        df  = pc.concat_row(df1, df2)
        self.assertEqual(isinstance(df, pd.DataFrame), True)

    def test_concat_row(self):
        df1 = pd.DataFrame([1,2,3])
        df2 = pd.DataFrame([4,5,6])
        df  = pc.concat_col(df1, df2)
        self.assertEqual(isinstance(df, pd.DataFrame), True)
    
    def test_inner_join(self):
        df1 = pd.DataFrame([1,2,3])
        df2 = pd.DataFrame([4,5,6])
        df  = pc.inner_join(df1, df2)
        self.assertEqual(isinstance(df, pd.DataFrame), True)

    def test_missing_value(self):

        # Remove missing values.
        df = pd.DataFrame([1,2,3,None])
        data = pc.missing_value(df)
        self.assertEqual(isinstance(df, pd.DataFrame), True)

        # fill out missing values with fill_value.
        df = pd.DataFrame([1,2,3,None])
        data = pc.missing_value(df, action="fill", fill_value=100)
        self.assertEqual(isinstance(df, pd.DataFrame), True)

if __name__ == '__main__':
    unittest.main()
