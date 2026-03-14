import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):

    bucket_name = "tarun-personal-cloud-storage-982189530346-us-east-1-an"
    file_name = "test-file.txt"
    content = "Hello from Lambda Cloud Storage Project!"

    s3.put_object(
        Bucket=bucket_name,
        Key=file_name,
        Body=content
    )

    return {
        'statusCode': 200,
        'body': json.dumps('File uploaded successfully')
    }