from plivo import plivoxml
from flask import request, Flask, Response

import plivo

client = plivo.RestClient("YOUR_AUTH_ID", "YOUR_AUTH_TOKEN")

# Machine detection using Call API

response = client.calls.create(
    from_="14152224444",  # The phone number to be used as the caller id
    to_=" 14152223333",  # The phone numer to which the all has to be placed
    answer_url="http://s3.amazonaws.com/static.plivo.com/answer.xml",  # The URL invoked by Plivo when the outbound call is answered
    answer_method="GET",  # The method used to call the answer_url
    machine_detection="true",  # Used to detect if the call has been answered by a machine. The valid values are true and hangup.
    machine_detection_time="10000",  # Time allotted to analyze if the call has been answered by a machine. The default value is 5000 ms.
    machine_detection_url="http://www.foo.com/machine_detection",  # A URL where machine detection parameters will be sent by Plivo.
    machine_detection_method="GET",
)
print(response)

# Sample successful output for Synchronous Request
# {
#    "message":"call fired",
#    "request_uuid":"9834029e-58b6-11e1-b8b7-a5bd0e4e126f",
#    "api_id":"97ceeb52-58b6-11e1-86da-77300b68f8bb"
# }

app = Flask(__name__)
# Machine Detection URL example


@app.route("/machine_detection/", methods=["POST", "GET"])
def machine_detection():
    from_number = request.args.get(
        "From"
    )  # The From number which is used to make the call.
    machine = request.args.get(
        "Machine"
    )  # This parameter will be true if a machine has been detected on the call.
    to_number = request.args.get("To")  # The number which is being called.
    call_uuid = request.args.get("CallUUID")  # The ID of the call.
    event = request.args.get(
        "Event"
    )  # The event of the notification. This parameter will always have the value MachineDetection.
    call_status = request.args.get(
        "CallStatus"
    )  # The status of the call. This will hold the value of in-progress.
    print(
        "From : %s To : %s  Machine : %s Call UUID : %s Event : %s Call Status : %s "
        % (from_number, to_number, machine, call_uuid, event, call_status)
    )


# Sample Output
# From : 2222222222 To : 1111111111 Machine : true Call UUID : 45704ba2-959f-11e4-802f-e9b058eeb9e5 Event : MachineDetection Call Status : in-progress

# As soon as the voicemail finishes speaking, and there is a silence for minSilence milliseconds,
# the next element in the XML is processed, without waiting for the whole period of length seconds to pass


@app.route("/detect/", methods=["GET", "POST"])
def detect():
    response = (
        plivoxml.ResponseElement()
        .add(
            plivoxml.WaitElement(
                silence=True,  # When silence is set to true, if no voice or sound is detected for minSilence milliseconds, end the wait and continue to the next element in the XML immediately
                min_silence="500",  # Time to wait in milliseconds
            ).set_length(
                10
            )  # Time to wait in seconds
        )
        .add(plivoxml.SpeakElement("Hello Voicemail!"))
    )
    return Response(response.to_string(), mimetype="application/xml")


# Sample Wait XML
# <Response>
#    <Wait length="10" silence="true" minSilence="500"/>
#    <Speak>Hello Voicemail!</Speak>
# </Response>

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)