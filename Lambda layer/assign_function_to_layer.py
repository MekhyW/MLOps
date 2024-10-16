import boto3
import os
from dotenv import load_dotenv

load_dotenv()

# Provide ARN and function name
layer_version_arn = (
    "arn:aws:lambda:us-east-2:820926566402:layer:layer_polarity_felipec13:1"
)
function_name = "polarity_felipec13"

# Create a Boto3 client for AWS Lambda
lambda_client = boto3.client(
    "lambda",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION"),
)

# Get the current configuration of the Lambda function
response = lambda_client.get_function(FunctionName=function_name)

# Retrieve the existing layers
layers = (
    response["Configuration"]["Layers"] if "Layers" in response["Configuration"] else []
)

print("Existing layers:")
print(layers)

# Append the layer ARN to the existing layers
layers.append(layer_version_arn)

# Update the function configuration with the new layers
lambda_response = lambda_client.update_function_configuration(
    FunctionName=function_name, Layers=layers
)

# Print response
print("Lambda response:\n", lambda_response)