from flask import Flask, Response, request
from plivo import plivoxml

app = Flask(__name__)


@app.route("/record/", methods=["POST", "GET"])
def record():

    # Generate a Record XML and ask the caller to leave
    # a message.

    # The recorded file will be sent to the 'action' URL

    response = plivoxml.ResponseElement()
    response.add(
        plivoxml.SpeakElement(
            "Please leave a message after the beep."
        )
    )
    response.add(
        plivoxml.RecordElement(
            action="http://foo.com/save_record_url/",
            method="GET",
            max_length=30,
            transcription_type="auto",
            transcription_url="http://foo.com/transcription/",
            transcription_method="GET",
        )
    )
    return Response(response.to_string(), mimetype="application/xml")


# Action URL Example

@app.route("/save_record_url/", methods=["GET"])
def save_record_url():
    if request.method == "GET":
        print(f"Record URL : {request.args.get('RecordUrl')}")
    elif request.method == "POST":
        print(f"Record URL :{request.form.get('RecordUrl')}")
    return Response("OK", mimetype="text/xml")


# Transcription URL Example

@app.route("/transcription/", methods=["GET", "POST"])
def transcription():
    if request.method == "GET":
        print("Transcription is : %s " % (request.args.get("transcription")))
    elif request.method == "POST":
        print("Transcription is : %s " % (request.form.get("transcription")))
    return Response("OK", mimetype="text/xml")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)


# Sample output
# <Response>
#    <Speak>Please leave a message after the beep.</Speak>
#    <Record action="https://foo.com/save_record_url/" maxLength="30" method="GET" transcriptionMethod="GET" transcriptionType="auto" 
#        transcriptionUrl="https://foo.com/transcription/" />
# </Response>

# Record URL : http://s3.amazonaws.com/recordings_2013/xxxxxxx-yyyyy-zzzzzz.mp3 
# Transcription is : Hello