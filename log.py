"""
Log manipulation. 

What you can do...

- Upload file to S3
"""

import boto3
import re
import pandas as pd
import pprint
pp = pprint.PrettyPrinter(indent=4)


def list_bucket_names():
    """List up bucket names. """

    s3 = boto3.resource('s3')
    for bucket in s3.buckets.all():
        print(bucket.name)


def upload_file(file_name, bucket_name, key_name):
    """Upload file to s3. 

    Parameters
    ----------
    file_name : str
        File name to upload.

    bucket_name : str
        S3 bucket name

    key_name : str
        key name on s3. Key name is equal to file name.
    """

    s3 = boto3.client('s3')

    with open(file_name) as f:
        s3.upload_fileobj(f, bucket_name, key_name)

    print("Successfully uploaded.")
    print("file   : {0}".format(file_name))
    print("bucket : {0}".format(bucket_name))
    print("key    : {0}".format(key_name))


def download_file(file_name, bucket_name, key_name):
    """Download object file from s3. 

    Parameters
    ----------
    file_name : str
        File name after downloading.

    bucket_name : str
        S3 bucket name.

    key_name : str
        Object file name on s3.
    """
    s3 = boto3.client('s3')
    with open(file_name, "wb") as f:
        s3.download_fileobj(bucket_name, key_name, f)

    print("Successfully Downloaded.")
    print("file   : {0}".format(file_name))
    print("bucket : {0}".format(bucket_name))
    print("key    : {0}".format(key_name))


def extract_ip_address(log_file):
    """Extract ip address from log file

    Parameter
    ---------
    log_file : 
        log file

    Return
    ------
    list : ip address list
    """
    with open(log_file) as f:
        content = f.readlines()

    ip_list = []
    for i in content:
        ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', i)
        ip_list.append(ip[0])

    return ip_list


def convert_from_list_to_df(list_val):
    """Convert from lsit to DataFrame"""

    return pd.DataFrame(list_val)


def grouping(df_data, col_num=0):
    """Counting

    Parameters
    ----------
    df_data : DataFrame

    col_num : integer
        Target column to count. 

    """
    pp.pprint(df_data.groupby(col_num).size())


if __name__ == '__main__':
    # upload_file()
    # upload_file("test.log", "log-files-1234", "test.log")
    # download_file("access_log", "log-files-1234", "access_log")
    ip_list = extract_ip_address("access_log")
    convert_from_list_to_df(ip_list)
