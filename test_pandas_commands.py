import unittest
import pandas_commands as pc
import pandas as pd

class TestPandasCommands(unittest.TestCase):

    def test_series_simple_df(self):
        self.assertEqual(len(pc.series_simple_df(10)), 10)

if __name__ == '__main__':
    unittest.main()
