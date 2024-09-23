import io
import os
import logging
import boto3
from dotenv import load_dotenv

load_dotenv()

bucket_name = "log-bucket-felipec13"
key = "log1"

# Function to write logs
def write_logs(body, bucket, key):
    s3 = boto3.client(
        "s3",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name=os.getenv("AWS_REGION"),
    )
    s3.put_object(Body=body, Bucket=bucket, Key=key)


log = logging.getLogger("my_logger")
string_io = io.StringIO()
handler = logging.StreamHandler(string_io)
log.addHandler(handler)

try:
    # Simulate exception
    raise ValueError
except ValueError:
    log.error("Missing value")
    log.error("Some error occurred!")
finally:
    # Persists logs to s3
    write_logs(body=string_io.getvalue(), bucket=bucket_name, key=key)