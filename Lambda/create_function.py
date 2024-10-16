import boto3
import os
from dotenv import load_dotenv

load_dotenv()

function_name = "sayHello_felipec13"

# Create a Boto3 client for AWS Lambda
lambda_client = boto3.client(
    "lambda",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION"),
)

# Lambda basic execution role
lambda_role_arn = os.getenv("AWS_LAMBDA_ROLE_ARN")

# Read the contents of the zip file that you want to deploy
# Inside the "my_lambda.zip" there is a "my_lambda.py" file with the
# "say_hello" function code
with open("my_lambda.zip", "rb") as f:
    zip_to_deploy = f.read()

lambda_response = lambda_client.create_function(
    FunctionName=function_name,
    Runtime="python3.9",
    Role=lambda_role_arn,
    Handler="my_lambda.say_hello", # Python file DOT handler function
    Code={"ZipFile": zip_to_deploy},
)

print("Function ARN:", lambda_response["FunctionArn"])