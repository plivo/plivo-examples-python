from flask import Flask, Response
import plivo, plivoxml

app = Flask(__name__)

@app.route("/hangup/", methods=['GET','POST'])
def hangup():

    # Generate a Hangup XML to reject an incoming call.

    params = {
        'reason': 'busy', # Specify the reason for hangup
        'schedule': '60' # Schedule the hangup
    }

    response = plivoxml.Response()
    response.addSpeak('This call will be hung up in 1 minute')    
    response.addHangup(**params)
    print response.to_xml()
    return Response(str(r), mimetype='text/xml')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

# Sample successful output
# <Response>
#   <Speak>This call will be hung up in 1 minute</Speak>
#   <Hangup reason="busy" schedule="60" />
# </Response>