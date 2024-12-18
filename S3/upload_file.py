import boto3
import os
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
)

s3.upload_file(
    "hello.txt",
    os.getenv("AWS_BUCKET_NAME"),
    "felipec13/hello.txt",
)