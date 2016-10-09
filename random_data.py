# -*- coding: UTF-8 -*-

"""
Generate random data with numpy module.
"""

import numpy as np


def generate_int(num, maximum):
    """
    Generate integer random data.
    Ex:
        generate_int(10, 9999)
    Parameters
    ----------
    num : integer
        Number of values to generate
    """
    return np.random.randint(0, maximum, num)
