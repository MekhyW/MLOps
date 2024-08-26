from my_ml_app import predict

while True:
    msg = input("Enter a message: ")
    if msg == "exit":
        break

    # Call Celery task
    payload = {"message": msg}
    result = predict.delay(payload)