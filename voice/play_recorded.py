from flask import Flask, Response
from plivo import plivoxml

app = Flask(__name__)


@app.route("/play/", methods=["GET", "POST"])
def play_xml():

    # Generate a Play XML with the details of audio file to play during the call

    response = plivoxml.ResponseElement()
    response.add(plivoxml.PlayElement("https://s3.amazonaws.com/Trumpet.mp3"))
    return Response(response.to_string(), mimetype="application/xml")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)


# Sample successful output
# <Response>
#	<Play>https://s3.amazonaws.com/plivocloud/Trumpet.mp3</Play>
# </Response>
