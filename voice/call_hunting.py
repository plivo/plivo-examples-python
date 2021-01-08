from plivo import plivoxml
from flask import Flask, Response

app = Flask(__name__)

# Simultaneous dialing is useful when there are SIP users and numbers that you want to dial.
# The first call that connects will cancel all other tries.


@app.route("/call_hunting/", methods=["GET", "POST"])
def call_hunting():
    response = plivoxml.ResponseElement()
    response.add(
        plivoxml.DialElement()
        .add(plivoxml.UserElement("sip:alice1234@phone.plivo.com"))
        .add(plivoxml.NumberElement("15671234567"))
        .add(plivoxml.UserElement("sip:john1234@phone.plivo.com"))
    ) 
    return Response(response.to_string(), mimetype="application/xml")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)


# Sample Dial XML output
# <Response>
#     <Dial>
#       <User>sip:alice1234@phone.plivo.com</User>
#       <Number>15671234567</Number>
#       <User>sip:john1234@phone.plivo.com</User>
#     </Dial>
# </Response>