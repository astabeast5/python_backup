import boto3

s3 = boto3.resource(
    "s3",
    endpoint_url="ENDPOINT_URL",
     aws_access_key_id="ACCESS ID",
     aws_secret_access_key="SECRET KEY",
     region_name="REGION"
 )

def show_buckets(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)

def create_bucket(s3):
    s3.create_bucket(Bucket="bucket_unique name_")
    print("Bucket created successfully")

create_bucket(s3)
show_buckets(s3)
