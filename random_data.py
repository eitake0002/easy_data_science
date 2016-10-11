# -*- coding: UTF-8 -*-

"""
Generate random data with numpy module.
"""

import numpy as np
import pandas as pd
import random
import datetime
import time

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
    """
    Generate random str data into list.

    Parameters
    ----------
    num : int
        Number of values to generate data.
    """
    random_ary = []
    for i in range(num):
        tmp = random_str(10)
        random_ary.append(tmp)
    return random_ary

def random_df_str(num):
    """
    Generate random str into DataFrame.

    Parameters
    ----------
    num : int
        Number of values to generate data.
    """
    np_data = random_list_str(num)
    return pd.DataFrame(np_data)

def random_datetime():
    """
    Generate random time object.
    The random range is between unix_time to now.

    Ex:
        random_datetime()

    """
    now = datetime.datetime.now()
    unix_time = time.mktime(now.timetuple())

    random_unix_time = np.random.randint(0, unix_time)
    return datetime.datetime.fromtimestamp(random_unix_time)

def random_datetime_list(num):
    """
    Generate random date object into list.

    Ex : 
        random_datetime_list(100)
    """
    datetime_list = []
    for i in range(num):
        datetime_list.append(random_datetime())

    return datetime_list

#def df_datetime_from_today():

#def df_datetime_from_to():

if __name__ == '__main__':
    import doctest
    doctest.testmod()
