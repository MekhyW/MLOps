from textblob import TextBlob
import json


def get_polarity(event, context):
    # Provide a body for the request!
    if "body" not in event:
        return {"error": "No body provided"}

    # Get the raw posted JSON
    raw_json = event["body"]

    # Load it into a Python dict
    body = json.loads(raw_json)

    if "phrase" not in body:
        return {"error": "No phrase provided"}

    phrase = body["phrase"]

    # Create a TextBlob object of the phrase
    blob = TextBlob(phrase)

    # Get the polarity score
    polarity = blob.polarity

    # Create a response object with the phrase and polarity
    res = {"phrase": phrase, "polarity": str(polarity)}

    # Determine the sentiment
    if polarity > 0.2:
        res["sentiment"] = "Positive sentiment"
    elif polarity >= -0.8:
        res["sentiment"] = "Neutral sentiment"
    else:
        res["sentiment"] = "Negative sentiment"

    return res