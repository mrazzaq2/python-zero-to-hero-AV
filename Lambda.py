import boto3

client = boto3.client('lambda')

response = client.create_function(
    FunctionName='string',
    Runtime='python3.6',
    Role='string',
    Handler='string',
    Code={
        'ZipFile': b'bytes',
        'S3Bucket': 'string',
        'S3Key': 'string',
        'S3ObjectVersion': 'string',
        'ImageUri': 'string'
    }
)