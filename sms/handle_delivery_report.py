from flask import Flask, request, make_response, Response

app = Flask(__name__)


@app.route("/delivery_report/", methods=["GET", "POST"])
def inbound_sms():
    # Sender's phone number
    from_number = request.values.get("From")
    # Receiver's phone number - Plivo number
    to_number = request.values.get("To")
    # The text which was received
    text = request.values.get("Text")
    # Message UUID
    uuid = request.values.get("MessageUUID")
    # Print the message
    print(
        "Message received - From: %s, To: %s, Text: %s, MessageUUID: %s"
        % (from_number, to_number, text, uuid)
    )

    return "Delivery status reported"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)


# Sample successful output
# Message received - From : 2222222222 To : 1111111111 Text: Hello world! Status : delivered MessageUUID : 53e6526a-8a7a-11e4-a77d-22000ae383ea

# Possible values for message status - "queued", "sent", "failed", "delivered", "undelivered" or "rejected"
