from flask import Flask, request, make_response, Response

app = Flask(__name__)


@app.route("/receive_sms/", methods=["GET", "POST"])
def inbound_sms():
    # Sender's phone number
    from_number = request.values.get("From")
    # Receiver's phone number - Plivo number
    to_number = request.values.get("To")
    # The text which was received
    text = request.values.get("Text")
    # Print the message
    print(
        "Message received - From: %s, To: %s, Text: %s" % (from_number, to_number, text)
    )

    return "Message Recevived"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)


# Sample successful output
# Message received - From:+14151112222 To:+14152223333 Text: Hello!
