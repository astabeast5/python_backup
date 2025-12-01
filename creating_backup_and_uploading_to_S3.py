import boto3

s3 = boto3.resource(
    "s3",
    endpoint_url="ENDPOINT URL",
     aws_access_key_id="ACCESS KEY",
     aws_secret_access_key="SECRET",
     region_name="REGION"
 )

def show_buckets(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)

def create_bucket(s3,bucket_name):
    s3.create_bucket(Bucket=bucket_name)
    print("Bucket created successfully")

def upload_backup(s3, file_name,bucket_name,key_name):
    
    data = open(file_name, 'rb') # data will be read in binary
    s3.Bucket(bucket_name).put_object(Key=key_name, Body=data)
    print("Backup uploaded successfully")

bucket_name = "python-for-learning"

create_bucket(s3,bucket_name)
file_name = "path"

upload_backup(s3,file_name, bucket_name,"my-backup.tar.gz")
show_buckets(s3)
