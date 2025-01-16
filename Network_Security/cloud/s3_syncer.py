# This module provides functionality to synchronize local folders with Amazon S3 buckets.


import os


class S3Sync:
    def sync_folder_to_s3(self,folder,aws_bucket_url):
        """
        Synchronizes a local folder to an S3 bucket.
        
        Parameters:
        folder (str): Path to the local folder to be uploaded.
        aws_bucket_url (str): S3 bucket URL where the folder will be uploaded.
        """

        command = f"aws s3 sync {folder} {aws_bucket_url} "
        os.system(command)

    def sync_folder_from_s3(self,folder,aws_bucket_url):
        """
        Synchronizes an S3 bucket to a local folder.
        
        Parameters:
        folder (str): Path to the local folder where data will be downloaded.
        aws_bucket_url (str): S3 bucket URL to download the data from.
        """
        
        command = f"aws s3 sync  {aws_bucket_url} {folder} "
        os.system(command)
