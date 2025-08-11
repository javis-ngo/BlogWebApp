import os

import boto3
from dotenv import load_dotenv

from utils.my_util import generate_random_string

def create_aws_instances():
    load_dotenv()

    endpoint_url = os.getenv('ENDPOINT_URL')
    region_name = os.getenv('REGION_NAME')
    dynamodb_client = boto3.client(
        'dynamodb',
        region_name=region_name,
        endpoint_url=endpoint_url
    )

    s3_client = boto3.client(
        's3',
        region_name=region_name,
        endpoint_url=endpoint_url
    )

    try:
        s3_client.create_bucket(Bucket=generate_random_string(10))
        dynamodb_client.create_table(
            TableName='blog',
            KeySchema=[
                {
                    'AttributeName': 'username',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'last_name',
                    'KeyType': 'RANGE'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'username',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'last_name',
                    'AttributeType': 'S'
                },
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )

    except Exception as e:
        print(f"Failed to create instance: {e}")
        return None, None

if __name__ == "__main__":
    endpoint, port = create_aws_instances()