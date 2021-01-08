from plivo import plivoxml
from flask import Flask, Response

app = Flask(__name__)

# Example for Basic Wait

@app.route("/basic_wait/", methods=["GET", "POST"])
def basic_wait():
    response = (
        plivoxml.ResponseElement()
        .add(plivoxml.SpeakElement("I will wait 6 seconds starting now."))
        .add(plivoxml.WaitElement(None).set_length(6))
        .add(plivoxml.SpeakElement("I just waited 6 seconds."))
    )
    return Response(response.to_string(), mimetype="application/xml")


# Sample Wait XML
# <Response>
#    <Speak>I will wait for 6 seconds</Speak>
#    <Wait length="6" />
#    <Speak>I just waited 6 seconds</Speak>
# </Response>

# Example for Delayed Call Answer

@app.route("/delayed_wait/", methods=["GET", "POST"])
def delayed_wait():
    response = (
        plivoxml.ResponseElement()
        .add(plivoxml.WaitElement(None).set_length(10))
        .add(plivoxml.SpeakElement("Hello, after 10 seconds"))
    )
    return Response(response.to_string(), mimetype="application/xml")


# Sample Wait XML
# <Response>
#    <Wait length="10" />
#    <Speak>Hello</Speak>
# </Response>

# Example for Beep Detection

@app.route("/beep_detection/", methods=["GET", "POST"])
def beep_det():
    response = (
        plivoxml.ResponseElement()
        .add(plivoxml.WaitElement(beep=True).set_length(10))
        .add(plivoxml.SpeakElement("Hello"))
    )
    return Response(response.to_string(), mimetype="application/xml")


# Sample Wait XML
# <Response>
#    <Wait length="10" beep="true" />
#    <Speak>Hello</Speak>
# </Response>

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug="True")


