
import json
import boto3
import logging
import botocore
logging.getLogger().setLevel(logging.INFO)
BUCKET_NAME ='dev-days-test'
KEY ="hello.txt"
s3 =boto3.resource('s3')
def lambda_handler(event, context):
    logging.info(event)
    try:
        s3.Bucket(BUCKET_NAME).download_file(KEY,'/tmp/hello_local.txt')
        temp_file='/tmp/hello_local.txt'
        file = open(temp_file, "r")

    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == '404':
           logging.error("the object doesnot exist")
        else:
             raise e
# TODO implement
    return {
            'statusCode': 200,
            'body': file.read()
    }
