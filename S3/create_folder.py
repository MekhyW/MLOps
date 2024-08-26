import boto3
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
)

res = s3.put_object(
    Bucket=os.getenv("AWS_BUCKET_NAME"),
    Key="felipec13/",
)

print("Answer:")
pprint(res)