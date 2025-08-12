import boto3
import os

endpoint_url = os.getenv('ENDPOINT_URL')
region_name = os.getenv('REGION_NAME')

dynamodb_resource = boto3.resource(
        'dynamodb',
        region_name=region_name,
        endpoint_url=endpoint_url
    )

table = dynamodb_resource.Table('BlogWebApp')

