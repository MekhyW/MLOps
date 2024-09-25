import boto3
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

lambda_response = lambda_client.create_function(
    FunctionName=function_name,
    Runtime="python3.10",
    Role=lambda_role_arn,
    Handler="word_count.word_count_handler",
    Code={"ZipFile": zip_to_deploy},
)