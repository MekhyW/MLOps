import requests

# Change the endpoint
url_endpoint = "https://bpsych3kx1.execute-api.us-east-2.amazonaws.com"

url = f"{url_endpoint}/polarity"

# Change the phrase
body = {"phrase": "This was the worst movie I watched this year, horrible!"}

resp = requests.post(url, json=body)

print(f"status code: {resp.status_code}")
print(f"text: {resp.text}")