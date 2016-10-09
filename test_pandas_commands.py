import unittest
import pandas_commands as pc
import pandas as pd

class TestPandasCommands(unittest.TestCase):

    def test_simple_df(self):
        self.assertEqual(len(pc.simple_df(10)), 10)

    def test_simple_df_with_col(self):
        self.assertEqual(len(pc.simple_df_with_col('id', 10)), 10)

if __name__ == '__main__':
    unittest.main()
