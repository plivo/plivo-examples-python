from plivo import plivoxml
from flask import Flask, Response, request, make_response
import traceback
import plivo

app = Flask(__name__)

# A call is made to the plivo number.
# The answer_url returns and XML that starts recording the session and then dials to another number.
# When the user pick up, the B Leg record starts and a music is played.

# The action URL of the Record tag will return the Session recording details


@app.route("/answer_incoming/", methods=["GET", "POST"])
def answer_incoming():
    response = plivoxml.ResponseElement()
    response.add(
        plivoxml.RecordElement(
            action="http://foo.com/record_action/",
            method="GET",
            record_session=True,
            callback_url="http://foo.com/record_action/",
            callback_method="GET",
            redirect=False,
        )
    )
    response.add(plivoxml.WaitElement(length="5"))
    response.add(plivoxml.SpeakElement("Connecting your call"))
    response.add(plivoxml.DialElement().add(plivoxml.NumberElement("15551234567")))
    return Response(response.to_string(), mimetype="application/xml")


# The Callback URL of Dial will make a request to the Record API which will record only the B Leg
# Play API is invoked which will play a music only on the B Leg.


@app.route("/dial_outbound/", methods=["GET", "POST"])
def dial_outbound():
    try:
        event = request.args.get("Event")
        call_uuid = request.args.get("DialBLegUUID")
        if event == "DialAnswer":
            auth_id = "YOUR_AUTH_ID"
            auth_token = "YOUR_AUTH_TOKEN"
            client = plivo.RestClient(auth_id, auth_token)
            response = client.calls.record(
                call_uuid=call_uuid,
                callback_url="https://www.foo.com/recording_callback/",
                callback_mathod="GET",
            )

            # Play audio over the call

            response = client.calls.play(
                call_uuid=call_uuid,
                urls="https://s3.amazonaws.com/plivocloud/music.mp3",
            )
            return Response(response, mimetype="text/plain")
        else:
            print("Invalid")
            return Response("INVALID", mimetype="text/plain")
    except Exception as e:
        print("\n".join(traceback.format_exc().splitlines()))


# The Callback URL of record api will return the B Leg record details.


@app.route("/recording_callback/", methods=["GET", "POST"])
def recording_callback():
    record_url = request.args.get("record_url")
    record_duration = request.args.get("recording_duration")
    record_id = request.args.get("recording_id")

    response = make_response("OK")
    response.headers["Content-type"] = "text/plain"
    print("Record URL : %s " % (record_url))
    print("Recording Duration : %s " % (record_duration))
    print("Recording ID : %s " % (record_id))
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug="True")
 

# Sample Output
# <Response>
#   <Record action="http://foo.com/record_action/" method="GET" redirect="false" recordSession="true" callbackUrl="http://foo.com/record_action/" callbackMethod="GET"/>
#   <Wait length="5"/>
#   <Speak>Connecting your call</Speak>
#   <Dial>
#     <Number>15551234567</Number>
#   </Dial>
# </Response>

# Output from the Record XML action URL
# Record URL : http://s3.amazonaws.com/recordings_2013/55556666-7777-11e4-a4c8-782bcb5bb8af.mp3 
# Recording Duration : -1 
# Recording ID : daddbf04-9585-11e4-a4c8-782bcb5bb8af 

# Output of the Record API request
#{
#     'message': 'async api spawned', 
#     'api_id': 'e3403906-9585-11e4-b153-22000abcaa64'
# }

# Output of the Play XML request
# {
#   "message": "play started",
#   "api_id": "07abfd94-58c0-11e1-86da-adf28403fe48"
# }

# Output of Record API Callback URL
# Record URL : http://s3.amazonaws.com/recordings_2013/11112222-4444-11e4-a4c8-782bcb5bb8af.mp3
# Recording Duration : 22 
# Recording ID : 693e61fd-8150-4091-a0f8-561d4a434288 

# Output of Record XML Callback URL
# Record URL : http://s3.amazonaws.com/recordings_2013/55556666-7777-11e4-a4c8-782bcb5bb8af.mp3 
# Recording Duration : 27 
# Recording ID : daddbf04-9585-11e4-a4c8-782bcb5bb8af 



