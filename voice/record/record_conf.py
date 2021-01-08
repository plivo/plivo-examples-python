import plivo
from flask import Flask, make_response, request, Response
from plivo import plivoxml

app = Flask(__name__)

# Generates a Conference XML

@app.route("/response/conference/", methods=["GET", "POST"])
def conference():
    response = plivoxml.ResponseElement().add(
        plivoxml.SpeakElement("You will now be placed into a demo conference.")
    )
    response.add(
        plivoxml.ConferenceElement(
            "demo",  # Conference Room name
            enter_sound="beep:1",  # Used to play a sound when a member enters the conference
            callback_url="https://www.foo.com/response/conf_callback/",  # If specified, information is sent back to this URL
            callback_method="GET",  # Method used to notify callbackUrl
        )
    )
    return Response(response.to_string(), mimetype="application/xml")

# Record API is called in the callback URL to record the conference.

@app.route("/response/conf_callback/", methods=["GET", "POST"])
def conf_callback():
    conf_name = request.form.get("ConferenceName")
    event = request.form.get("Event")
    response = make_response("OK")
    response.headers["Content-type"] = "text/plain"
    print("Conference Name : %s " % (conf_name))

    # The recording starts when the user enters the conference room

    if event == "ConferenceEnter":
        auth_id = "YOUR_AUTH_ID"
        auth_token = "YOUR_AUTH_TOKEN"

        client = plivo.RestClient(auth_id, auth_token)
        response = client.conferences.record(
            conference_name="testing",  # Conference Room name to be recorded
        )
        return str(response)
    else:
        print("invalid")
        return Response("INVALID", mimetype="text/plain")


# Sample Output
# <Response>
#   <Speak>You will now be placed into a demo conference.</Speak>
#   <Conference enterSound="beep:1" callbackUrl="https://www.foo.com/response/conf_callback/" callbackMethod="GET">demo</Conference>
# </Response>


# {
# 	"api_id": "2867b6e2-58c3-11e1-86da-adf28403fe48",
# 	"message": "conference recording started",
# 	"recording_id": "93bc7c6a-3b2b-11e3",
# 	"url": "http://s3.amazonaws.com/recordings_2013/93bc7c6a-3b2b-11e3.mp3",
# }
