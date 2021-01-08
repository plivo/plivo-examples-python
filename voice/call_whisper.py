from plivo import plivoxml
from flask import Flask, Response

app = Flask(__name__)


@app.route("/call_whisper/", methods=["GET", "POST"])
def call_whisper():
    response = plivoxml.ResponseElement()
    response.add(
        plivoxml.DialElement(
            confirm_key="5",  # The digit to be pressed by the called party to accept the call.
            confirm_sound="http://foo.com/confirm_sound/"  # A remote URL fetched with POST HTTP request which must return an
            # XML response with Play, Wait and/or Speak elements only.
        )
        .add(plivoxml.NumberElement("18217654321"))
        .add(plivoxml.NumberElement("15671234567"))
        .add(plivoxml.NumberElement("15671289109"))
    )
    return Response(response.to_string(), mimetype="application/xml")

@app.route("/confirm_sound/", methods=["GET", "POST"])
def confirm_sound():
    response = plivoxml.ResponseElement().add(
        plivoxml.SpeakElement("Press 5 to answer the call.")
    )
    return Response(response.to_string(), mimetype="application/xml")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8040)


# Sample output
# <Response>
#     <Dial confirmSound="http://foo.com/confirm_sound/" confirmKey="5">
#         <Number>18217654321</Number>
#         <Number>15671234567</Number>
#         <Number>15671289109</Number>
#     </Dial>
# </Response>

# <Response>
#    <Speak>Press 5 to answer the call</Speak>
# </Response>
