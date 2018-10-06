"""
Log manipulation. 

What you can do...

- Upload file to S3
"""

import boto3


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


if __name__ == '__main__':
    # upload_file()
    # upload_file("test.log", "log-files-1234", "test.log")
    download_file("test.log", "log-files-1234", "test.log")
