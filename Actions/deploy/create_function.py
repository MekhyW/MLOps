import boto3
import boto3.exceptions
import os

function_name = "wc_felipec13"

lambda_client = boto3.client(
    "lambda",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION"),
)

lambda_role_arn = os.getenv("AWS_LAMBDA_ROLE_ARN")

with open("word_count.zip", "rb") as f:
    zip_to_deploy = f.read()

try:
    lambda_response = lambda_client.create_function(
        FunctionName=function_name,
        Runtime="python3.10",
        Role=lambda_role_arn,
        Handler="word_count.word_count_handler",
        Code={"ZipFile": zip_to_deploy},
    )
except boto3.exceptions.botocore.exceptions.ClientError as e:
    if e.response["Error"]["Code"] == "ResourceConflictException":
        print("Function already exists")
    else:
        raise e