import plivo
from plivo import plivoxml
from flask import Flask, Response, request

app = Flask(__name__)

# When the call is answered, a text is played which prompts the user to press 1 to record the call.
# Once the digit is pressed, the Record API request is made and the recording starts.


@app.route("/record_api/", methods=["POST", "GET"])
def record_api():
    response = plivoxml.ResponseElement()
    response.add(
        plivoxml.GetDigitsElement(
            action="http://www.foo.com/record_action/",
            method="GET",
            timeout="7",
            num_digits="1",
            retries="1",
            redirect=False,
        ).add(
            plivoxml.SpeakElement(
                "Press 1 to record this call"
            )
        )
    )
    response.add(plivoxml.SpeakElement("Input not received. Thank you"))
    return Response(response.to_string(), mimetype="application/xml")


# The Record API is invoked by the Get Digits action URL

@app.route("/record_action/", methods=["POST", "GET"])
def record_action():
    digit = request.args.get("Digits")
    call_uuid = request.args.get("CallUUID")
    auth_id = "YOUR_AUTH_ID"
    auth_token = "YOUR_AUTH_TOKEN"
    print("Call UUID is : %s " % (call_uuid))
    print("Digit pressed is : %s " % (digit))
    client = plivo.RestClient(auth_id, auth_token)
    if digit == "1":
        response = client.calls.record(
            call_uuid=call_uuid,  # ID of the call
        )
        print(response)
        return Response(response.to_string(), mimetype="application/xml")
    else:
        print("Wrong Input")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug="True")


# Sample successful output
# <Response>
#    <GetDigits action="http://www.foo.com/recording_action/" method="GET" numDigits="1" redirect="false" retries="1" timeout="7">
#        <Speak>Press 1 to record this call</Speak>
#    </GetDigits>
#    <Speak>Input not received. Thank you</Speak>
# </Response>

# Call UUID is : 2a2875b6-9592-11e4-8b35-cd90edc77fa9 
# Digit pressed is : 1 

# Response from record api
# {
#   "url": "http://s3.amazonaws.com/recordings_2013/48dfaf60-3b2a-11e3.mp3",
#   "message": "call recording started",
#   "recording_id": "48dfaf60-3b2a-11e3",
#   "api_id": "c7b69074-58be-11e1-86da-adf28403fe48"
# }
