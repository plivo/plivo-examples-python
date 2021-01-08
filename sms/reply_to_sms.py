from flask import Flask, request, Response
from plivo import plivoxml

app = Flask(__name__)


@app.route("/reply_sms/", methods=["GET", "POST"])
def inbound_sms():
    # Sender's phone number
    from_number = request.values.get("From")
    # Receiver's phone number - Plivo number
    to_number = request.values.get("To")
    # The text which was received
    text = request.values.get("Text")
    # Print the message
    print("Message received - From: %s, To: %s, Text: %s" % (from_number, to_number, text))

    # send the details to generate an XML
    response = plivoxml.ResponseElement()
    response.add(
        plivoxml.MessageElement(
            "Thank you, we have received your request",  # The text to be sent
            src=to_number,  # Sender's phone number
            dst=from_number,  # Receiver's phone Number
            type="sms",
            callback_url="http://foo.com/sms_status/",
            callback_method="POST",
        )
    )
    print(response.to_string())  # Prints the XML
    # Returns the XML
    return Response(response.to_string(), mimetype="application/xml")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)


# Sample successful output
# Message received - From:+14151112222 To:+14152223333 Text: Hello!
#<Response>
#   <Message callbackMethod="POST" callbackUrl="http://foo.com/sms_status/" dst="+14151112222" src="+14152223333">Thank you, we have received your request</Message>
#</Response>
