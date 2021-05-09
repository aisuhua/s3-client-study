import boto3
from botocore.client import Config
 
 
# Config
s3endpoint = 'http://s3-cn-south-1.qiniucs.com'
s3region = 'cn-south-1'
s3accessKeyId = 'yFUjBpUCoWIXNluk8IbHPmEa4AzycZS7Kz7Gsw9e'
s3SecretKeyId = 'ydmvlTiynRS8sSSfXndEvsyL8TFD4enTvBhGXFSv'
 
 
# Use S3 client
s3client = boto3.client(
        's3',
        aws_access_key_id = s3accessKeyId,
        aws_secret_access_key = s3SecretKeyId,
        endpoint_url = s3endpoint,
        region_name = s3region
     )

with open("demo.py", "rb") as f:
    s3client.upload_fileobj(f, "suhuatest", "demo.py")
