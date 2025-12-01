"""
For this script to work you should install boto3 in your environment
"""
import boto3

s3 = boto3.resource(
    "s3",
    endpoint_url="Endpoint URL here",
     aws_access_key_id="AWS Access ID",
     aws_secret_access_key="AWS Secret Key",
     region_name="Region "
 )

def show_buckets(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)

show_buckets(s3)
