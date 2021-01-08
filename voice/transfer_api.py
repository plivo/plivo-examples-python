import plivo
from plivo import plivoxml
from flask import Flask, Response, request

app = Flask(__name__)

# When the call is answered, a text is played which prompts the user to press 1 to transfer the call.
# Once the digit is pressed, the transfer API request is made and the call is transfered to another number.


@app.route("/call_transfer/", methods=["POST", "GET"])
def call_transfer():
    response = plivoxml.ResponseElement()
    response.add(
        plivoxml.GetDigitsElement(
            action="http://www.foo.com/transfer_action",
            method="POST",
            timeout="7",
            num_digits="1",
            retries="1",
            redirect=False,
        ).add(
            plivoxml.SpeakElement(
                "Press 1 to transfer this call"
            )
        )
    )
    response.add(plivoxml.SpeakElement("Input not received. Thank you"))
    print(response.to_string())
    return Response(response.to_string(), mimetype="application/xml")


# The Transfer API is invoked by the Get Digits action URL


@app.route("/transfer_action/", methods=["POST", "GET"])
def transfer_action():
    digit = request.args.get("Digits")
    call_uuid = request.args.get("CallUUID")
    auth_id = "Your AUTH_ID"
    auth_token = "Your AUTH_TOKEN"
    print("Call UUID is : %s " % (call_uuid))
    print("Digit pressed is : %s " % (digit))

    client = plivo.RestClient(auth_id, auth_token)
    if digit == "1":
        response = client.calls.transfer(
            legs="aleg",  # leg of the call to be transferred.
            aleg_url="http://aleg.url",  # URL to transfer for aleg
            call_uuid=call_uuid,  # ID of the call
        )
    else:
        print("Wrong Input")
    return Response(response.to_string(), mimetype="application/xml")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug="True")


# Sample Output
# <Response>
#    <GetDigits action="http://www.foo.com/transfer_action/" method="GET" numDigits="1" redirect="false" retries="1" timeout="7">
#        <Speak>Press 1 to transfer this call</Speak>
#    </GetDigits>
# </Response>

# Call UUID is : e66aa1a0-9587-11e4-9d37-c15e0b562efe 
# Digit pressed is : 1

# {
# "message": "call transfered",
# "api_id": "08c94608-58bd-11e1-86da-adf28403fe48"
# }

# <Response>
#    <Speak>Connecting your call..</Speak>
#    <Dial>
#        <Number>1111111111</Number>
#    </Dial>
# </Response>