"""
This script deletes S3 buckets with confirmation prompt

"""
import boto3

s3 = boto3.resource(
    "s3",
    endpoint_url="ENDPOINT URL",
    aws_access_key_id="ACCESS KEY",
    aws_secret_access_key="SECRET KEY",
    region_name="REGION"
)

def show_buckets(s3):
    buckets = list(s3.buckets.all())
    if not buckets:
        print("No buckets found")
        return []
    
    print("Available buckets:")
    for i, bucket in enumerate(buckets, 1):
        print(f"{i}. {bucket.name}")
    return buckets

def delete_bucket(s3, bucket_name):
    bucket = s3.Bucket(bucket_name)
    
    # Delete all objects first
    bucket.objects.all().delete()
    
    # Delete the bucket
    bucket.delete()
    print(f"Bucket '{bucket_name}' deleted successfully")

def main():
    buckets = show_buckets(s3)
    
    if not buckets:
        return
    
    bucket_name = input("\nEnter bucket name to delete: ")
    
    # Check if bucket exists
    bucket_names = [bucket.name for bucket in buckets]
    if bucket_name not in bucket_names:
        print("Bucket not found!")
        return
    
    # Confirmation prompt
    confirm = input(f"Are you sure you want to delete '{bucket_name}'? (yes/no): ")
    
    if confirm.lower() == 'yes':
        delete_bucket(s3, bucket_name)
    else:
        print("Deletion cancelled")

if __name__ == "__main__":
    main()
