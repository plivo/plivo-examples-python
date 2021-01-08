from plivo import plivoxml
from flask import Flask, Response

app = Flask(__name__)


@app.route("/seq_dial/", methods=["GET", "POST"])
def dial_status():

    # This example calls out to a list of phone numbers sequentially.
    # The first call is made to the number in order, with a timeout value to 20s.
    # If the call is not answered within 20s, Plivo will then dial out to the second number.

    response = plivoxml.ResponseElement()
    response.add(
        plivoxml.DialElement(action="http://foo.com/dial_action/", time_limit=20).add(
            plivoxml.NumberElement("18217654321")
        )
    )
    response.add(plivoxml.DialElement().add(plivoxml.NumberElement("15671234567")))
    return Response(response.to_string(), mimetype="application/xml")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)


# Sample output
# <Response>
#   <Dial action="http://foo.com/dial_action/" timeLimit="20">
#     <Number>18217654321</Number>
#   </Dial>
#   <Dial>
#     <Number>15671234567</Number>
#   </Dial>
# </Response>
