import plivo
from flask import Flask, Response

app = Flask(__name__)

# When the call is answered, a text is played which prompts the user to press 1 to transfer the call.
# Once the digit is pressed, the transfer API request is made and the call is transfered to another number.

@app.route('/call_transfer/', methods=['POST', 'GET'])
def call_transfer():

    response = plivoxml.Response()
    getdigits_action_url = url_for('transfer_action', _external=True)
    getDigits = plivoxml.GetDigits(action=getdigits_action_url,
            method='GET', timeout=7, numDigits=1,
            retries=1, redirect='false')
    getDigits.addSpeak("Press 1 to transfer this call")
    response.add(getDigits) 
    params = {
        'length' : "10" # Time to wait in seconds
    } 
    response.addWait(**params)
    print response.to_xml()
    return Response(str(response), mimetype='text/xml')

# The Transfer API is invoked by the Get Digits action URL

@app.route('/transfer_action/', methods=['POST', 'GET'])
def transfer_action():
    digit = request.args.get('Digits')
    call_uuid = request.args.get('CallUUID')
    auth_id = "Your AUTH_ID"
    auth_token = "Your AUTH_TOKEN"
    print "Call UUID is : %s " % (call_uuid)
    print "Digit pressed is : %s " % (digit)
    p = plivo.RestAPI(auth_id, auth_token)
    if digit == "1":
        params = {
            'call_uuid' : call_uuid, # ID of the call
            'aleg_url' : "https://morning-ocean-4669.herokuapp.com/connect/", # URL to transfer for aleg
            'aleg_method' : "GET" # ethod to invoke the aleg_url
        }
        response = p.transfer_call(params)
    else :
        print "Wrong Input"
    print str(response)
    return Response(str(response), mimetype='text/plain')

if __name__=='__main__':
    app.run(host='0.0.0.0',debug='True')

# Sample Output
# <Response>
#    <GetDigits action="http://morning-ocean-4669.herokuapp.com/transfer_action/" method="GET" numDigits="1" redirect="false" retries="1" timeout="7">
#        <Speak>Press 1 to transfer this call</Speak>
#    </GetDigits>
#    <Wait length="10" />
# </Response>

# Call UUID is : e66aa1a0-9587-11e4-9d37-c15e0b562efe 
# Digit pressed is : 1

# (202, {
#        u'call_uuids': [
#            u'e66aa1a0-9587-11e4-9d37-c15e0b562efe'
#        ], 
#        u'message': u'transfer executed', 
#        u'api_id': u'eb8c80ae-9587-11e4-b423-22000ac8a2f8'
#    }
# )
# <Response>
#    <Speak>Connecting your call..</Speak>
#    <Dial>
#        <Number>1111111111</Number>
#    </Dial>
# </Response>