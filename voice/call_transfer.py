from plivo import plivoxml
from flask import Flask, Response

app = Flask(__name__)


@app.route("/call_transfer/", methods=["GET", "POST"])
def call_transfer():
    response = plivoxml.ResponseElement()
    response.add(
        plivoxml.SpeakElement("Please wait while you call is being transferred.")
    )
    response.add(plivoxml.RedirectElement("http://foo.com/connect/"))
    return Response(response.to_string(), mimetype="application/xml")


@app.route("/connect/", methods=['GET', 'POST'])
def connect():
    response = plivoxml.ResponseElement()
    response.add(plivoxml.SpeakElement("Connecting your call"))
    response.add(
        plivoxml.DialElement(
            action="http://foo.com/dial_status/", method="GET", redirect=True
        ).add(plivoxml.NumberElement("15671234567"))
    )
    return Response(response.to_string(), mimetype="application/xml")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

# Sample output for Redirect XML
# <Response>
#    <Speak>Please wait while you call is being transferred</Speak>
#    <Redirect>https://foo.com/connect/</Redirect>
#</Response>

# Sample output for Dial XML
# <Response>
#    <Speak>Connecting your call..</Speak>
#    <Dial action="https://foo.com/dial_status/" method="GET" redirect="true">
#        <Number>15671234567</Number>
#    </Dial>
#</Response>
