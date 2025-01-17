import json
import boto3
import base64
from botocore.exceptions import ClientError

def lambda_handler(event):
    file_content = event['file_content']  
    bucket_name = event['bucket_name']    
    file_name = event['file_name']        
    try:
        decoded_file = base64.b64decode(file_content)
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'File decoding failed', 'details': str(e)})
        }
    s3 = boto3.client('s3')
    try:
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=decoded_file)
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'File uploaded successfully to ' + bucket_name})
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'S3 upload failed', 'details': str(e)})
        }
