from flask import Flask, Response
from plivo import plivoxml

app = Flask(__name__)


@app.route("/dial/", methods=["GET", "POST"])
def dial():

    # When an outbound call is made and then connected different number using Dial element,
    # you can play a custom caller tone using the dialMusic attribute

    response = plivoxml.ResponseElement()
    response.add(
        plivoxml.DialElement(dial_music="http://foo.com/dial_music/").add(
            plivoxml.NumberElement("15671234567")
        )
    )
    return Response(response.to_string(), mimetype="application/xml")

# Sample Dial XML
# <Response>
#     <Dial dialMusic="http://foo.com/dial_music/">
#         <Number>15671234567</Number>
#     </Dial>
# </Response>

# Play XML is returned on the dialMusic Url

@app.route("/dial_music/", methods=["GET", "POST"])
def custom_tone():

    response = plivoxml.ResponseElement()
    response.add(plivoxml.PlayElement("https://s3.amazonaws.com/Trumpet.mp3"))
    return Response(response.to_string(), mimetype="application/xml")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8040)


# Sample successful output
# <Response>
#     <Play>https://s3.amazonaws.com/plivocloud/Trumpet.mp3</Play>
# </Response>
