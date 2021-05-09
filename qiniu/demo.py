import boto3
from botocore.client import Config
 
 
# Config
s3endpoint = 'http://s3-cn-east-1.qiniucs.com'
s3region = 'cn-east-1'
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
 
 
# List buckets
buckets = s3client.list_buckets()
 
# Output the bucket names
for bucket in buckets['Buckets']:
    print(bucket["Name"])
 
 
# Use S3 resource
s3resource = boto3.resource('s3',
    endpoint_url = s3endpoint,
    region_name = s3region,
    aws_access_key_id = s3accessKeyId,
    aws_secret_access_key = s3SecretKeyId
    )
 
 
# List buckets
buckets = s3resource.buckets.all()
 
# Output the bucket names
for bucket in buckets:
    print(bucket.name)
