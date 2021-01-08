import plivo
from flask import Flask, Response, request
from plivo import plivoxml

app = Flask(__name__)


@app.route("/speak_api/", methods=["GET", "POST"])
def speak_api():
    response = plivoxml.ResponseElement()
    response.add(
        plivoxml.GetDigitsElement(
            action="speak_action",
            method="POST",
            timeout="7",
            num_digits="1",
            retries="1",
            redirect=False,
        ).add(
            plivoxml.SpeakElement(
                "Press 1 to listen to a message"
            )
        )
    )
    response.add(plivoxml.SpeakElement("Input not received. Thank you"))
    print(response.to_string())
    return Response(response.to_string(), mimetype="application/xml")


@app.route("/speak_action/", methods=["GET", "POST"])
def speak_action():
    digit = request.args.get("Digits")
    call_uuid = request.args.get("CallUUID")
    auth_id = "YOUR_AUTH_ID"
    auth_token = "YOUR_AUTH_TOKEN"
    print("Call UUID is : %s " % (call_uuid))
    print("Digit pressed is : %s " % (digit))
    client = plivo.RestClient(auth_id, auth_token)
    if digit == "1":
        response = client.calls.speak(
            call_uuid=call_uuid,  # ID of the call
            text="Hello from Speak API",  # Text to be played.
            voice="WOMAN",  # The voice to be used, can be MAN,WOMAN. Defaults to WOMAN.
            language="en-GB",  # The language to be used
        )
        print(response)
        return Response(response, mimetype="text/plain")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug="True")


# Sample successful output
# <Response>
#    <GetDigits action="/speak_action/" method="GET" numDigits="1" redirect="false" retries="1" timeout="7">
#        <Speak>Press 1 to listen to a message</Speak>
#    </GetDigits>
# </Response>

# Call UUID is : 01d03d86-958f-11e4-a25f-c374cdd23d80 
# Digit pressed is : 1 

# {
#   "message": "speak started",
#   "api_id": "07abfd94-58c0-11e1-86da-adf28403fe48"
# }
