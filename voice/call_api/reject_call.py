from flask import Flask, Response
from plivo import plivoxml

app = Flask(__name__)

@app.route("/hangup/", methods=['GET','POST'])
def hangup():
    # Generate a Hangup XML to reject an incoming call.
    response = plivoxml.ResponseElement()
    
    response.add(
    plivoxml.HangupElement(
        schedule=60,  # Schedule the hangup
        reason="rejected",  # Specify the reason for hangup
        )
    )
    response.add(plivoxml.SpeakElement("This call will hang up after a minute.", loop=0))
    print(response.to_string())
    return Response(response.to_string(), mimetype="application/xml")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

# Sample successful output
# <Response>
#     <Hangup schedule="60" reason="rejected" />
#     <Speak loop="0">This call will be hung up after a minute</Speak>
# </Response>