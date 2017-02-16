# script initialize read.
# Ex: $ ipython -i init.py

# read other oepn source modules.
import inspect
import imp
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sys import getsizeof

# read easy_data_science modules.
import random_data as rd
import data_frame

# set random dataframe
df1 = rd.random_int(10, 100, "df", ["col_1"])
df2 = rd.random_int(10, 100, "df", ["col_2"])

# set random ndarray
np1 = rd.random_int(1000)
np2 = rd.random_int(1000)

# describe, set percentile
#df1.describe(percentiles=[.05, .25, .5, .75, .95])
per = [.05, .025, .5, .75, .95]

def check_bin(decimal_var, n=4):
    print(decimal_var)
    print(id(decimal_var))
    
    binary_data   = format(id(decimal_var), '016b')
    print(binary_data)
    length        = len(binary_data)
    
    if length == 47:
        binary_data = '0' + binary_data
    
    binary_length = [ binary_data[i:i+n] for i in range(0, length, n) ]
    print(binary_length)
    print(len(binary_data))
