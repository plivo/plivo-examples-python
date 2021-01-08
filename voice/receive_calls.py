from flask import Flask, Response
from plivo import plivoxml

app = Flask(__name__)


@app.route("/speak/", methods=["GET", "POST"])
def speak_xml():

    # Generate a Speak XML with the details of the text to play on the call.

    response = plivoxml.ResponseElement().add(
        plivoxml.SpeakElement("Hello, Welcome to Plivo.")
    )
    return Response(response.to_string(), mimetype="application/xml")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)


# Sample successful output
# <Response>
#    <Speak>Hello, Welcome to Plivo.</Speak>
# </Response>