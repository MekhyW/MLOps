import boto3
from botocore import UNSIGNED
from botocore.config import Config

# Disable authentication
s3 = boto3.client(
    "s3",
    config=Config(signature_version=UNSIGNED),
)

# Bucket name
bucket = "atd-insper"

# Public file at bucket
key = "aula04/alice_wonderland.txt"

response = s3.get_object(
    Bucket=bucket,
    Key=key,
)

content = response["Body"].read().decode("utf-8")

print(f"File Content:\n{content}")