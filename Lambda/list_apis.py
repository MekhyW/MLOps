import boto3
import os
from dotenv import load_dotenv

load_dotenv()

api_gateway = boto3.client(
    "apigatewayv2",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION"),
)

response = api_gateway.get_apis(MaxResults="2000")

# Show APIs name and endpoint
print("APIs:")
for api in response["Items"]:
    print(f"- {api['Name']} ({api['ApiEndpoint']})")