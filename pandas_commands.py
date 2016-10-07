# -*- coding: UTF-8 -*-

import pymysql.cursors
import pandas as pd
import os

# ---------------------------------------------------------------------
# MySQL
# ---------------------------------------------------------------------

# Paste below variables to ~/.bash_profile first.
"""
export db_host=db_host
export db_name=database
export db_user=user
export db_pass=pass
export db_charset=utf8
"""


def mysql_connect():
    """
    MySQL connection.
    Above parameters must be set to ~/.bash_profile first.
    """

    db_host = os.environ["db_host"]
    db_name = os.environ["db_name"]
    db_user = os.environ["db_user"]
    db_pass = os.environ["db_pass"]
    db_charset = os.environ["db_charset"]

    return pymysql.connect(
        host=db_host,
        db=db_name,
        user=db_user,
        # passwd = user,
        charset=db_charset,
    )


def table_data(table):
    """
    Execute SQL with pandas.

    Parameters
    ----------
    table : string
        Table name.
    """
    qry = "SELECT * FROM {0}".format(table)
    return pd.read_sql(qry, connector)


def table_data_chunk(table, chunksize):
    """
    Execute SQL with chunk.

    Parameters
    ----------
    table : string
        Table name.
    chunksize : integer
        Number of chunk size to process.
    """
    qry = "SELECT * FROM {0}".format(table)
    return pd.read_sql(qry, connector, chunksize=chunksize)

# ---------------------------------------------------------------------
# csv
# ---------------------------------------------------------------------


def read_csv(csv_path):
    """
    Read csv

    Prameters
    ---------
    csv_path : str
        csv file path to read.
    """
    pd.read_csv(csv_path)

# ---------------------------------------------------------------------
# Generate random/test data
# ---------------------------------------------------------------------

def series_simple_df(num):
    """
    Generate simple dataframe

    Parameters
    ----------
    num : integer
        Number of craete data.
    """
    return pd.DataFrame([i for i in range(num)])

# ---------------------------------------------------------------------
# Search data
# ---------------------------------------------------------------------


def more_than_num(df, col, num):
    """
    Get more than num data from dataframe.

    Ex:
        more_than_num(df, "id", 1)

    Parameters
    ----------
    df  : DataFrame
        DataFrame
    col : column name
        Column name.
    num : integer
        More than value
    """
    return df.query("{0} > {1}".format(col, num))


def less_than_num(df, col, num):
    """
    Get less than num data from dataframe.

    Ex:
        more_than_num(df, "id", 100)

    Parameters
    ----------
    df  : DataFrame
        DataFrame
    col : column name
        Column name.
    num : integer
        Less than value
    """
    return df.query("{0} < {1}".format(col, num))


def between_num(df, col, low, high):
    """
    Get between data from dataframe.

    Ex:
        between_num(df, "id", 1, 100)

    Parameters
    ----------
    df  : DataFrame
        DataFrame
    col : column name
        Column name.
    low : integer
        Less than value
    high : integer
        More than value
    """
    return df.query("{1} > {2} & {1} < {3}".format(col, low, high))
