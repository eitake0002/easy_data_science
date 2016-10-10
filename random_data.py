# -*- coding: UTF-8 -*-

"""
Generate random data with numpy module.
"""

import numpy as np
import pandas as pd

def rand_int(num, maximum):
    """
    Generate integer random data.

    >>> len(rand_int(100, 100))
    100

    Parameters
    ----------
    num : integer
        Number of values to generate
    """
    return np.random.randint(0, maximum, num)

def random_df_int(num, maximum):
    """
    Generate random int data into DataFrame.

    >>> len(random_df_int(100, 100))
    100

    Parameters
    ----------
    num : integer
        Number of values to generate.
    """
    random_data_np = np.random.randint(0, maximum, num)
    return pd.DataFrame(random_data_np)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
