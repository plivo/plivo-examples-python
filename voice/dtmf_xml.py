import plivoxml
from flask import Flask, Response

app = Flask(__name__)

# Example for DTMF XML
# The DTMF element is used to send digits on a live call. 
# This will usually be used to automate the process of navigating through an external phone tree (IVR).

@app.route('/dtmf/', methods=['GET','POST'])
def dtmf():
    r = plivoxml.Response()
    r.addSpeak("Sending Digits")
    r.addDTMF("12345")
    print r.to_xml()
    return Response(str(r), mimetype='text/xml')

if __name__=='__main__':
    app.run(host='0.0.0.0',debug='True')

# Sample DTMF XML
# <Response>
#    <Speak>Sending Digits</Speak>
#    <DTMF>12345</DTMF>
# </Response>