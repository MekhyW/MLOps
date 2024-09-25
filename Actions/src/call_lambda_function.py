import io
import boto3
import json

function_name = "wc_felipec13"

# Create a Boto3 client for AWS Lambda
lambda_client = boto3.client("lambda")

msg = {"body": "hello from mars"}

try:
    print(f"Message:\n{msg}")

    response = lambda_client.invoke(
        FunctionName=function_name,
        InvocationType="RequestResponse",
        Payload=json.dumps(msg),
    )

    payload = response["Payload"]

    txt = io.BytesIO(payload.read()).read().decode("utf-8")
    print(f"\nResponse:\n{txt}")
except Exception as e:
    print(e)