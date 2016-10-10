# -*- coding: UTF-8 -*-

"""
Generate random data with numpy module.
"""

import numpy as np
import pandas as pd
import random

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

def random_str(num):
    """
    Generate random string.

    Parameters 
    ----------
    num : integer
        Number of values to generate data.
    """
    str_list = "asdfghjklqwertyuiopzxcvbnm1234567890ASDFGHJKLZXCVBNMQWERTYUIOP"
    rand_str = ""

    for i in range(num):
        rand_str += random.choice(str_list)

    return rand_str

def random_list_str(num):
    random_ary = []
    for i in range(num):
        tmp = random_str(10)
        random_ary.append(tmp)
    return random_ary

if __name__ == '__main__':
    import doctest
    doctest.testmod()
