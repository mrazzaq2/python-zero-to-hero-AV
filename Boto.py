import boto3
import requests

client = boto3.client('s3')

response = client.create_bucket(
    Bucket='awsbucketforfirsttimee1',
)

response = client.get_bucket_acl(
    Bucket='awsbucketforfirsttimee1',
)

print(response["response"])
#print(response)
#print(response.json())
