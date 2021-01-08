from flask import Flask, Response
from plivo import plivoxml

app = Flask(__name__)


@app.route("/connect/", methods=["GET", "POST"])
def connect():

    # Generate a Dial XML with the details of the number to call

    response = plivoxml.ResponseElement()
    response.add(plivoxml.SpeakElement("Connecting your call.."))
    response.add(plivoxml.DialElement().add(plivoxml.NumberElement("15671234567")))
    return Response(response.to_string(), mimetype="application/xml")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

# Sample successful output
# <Response>
#   <Speak>Connecting your call..</Speak>
#   <Dial>
#     <Number>15671234567</Number>
#   </Dial>
# </Response>
