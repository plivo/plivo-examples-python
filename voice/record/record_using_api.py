import plivo
from flask import Flask, Response, request, url_for

app = Flask(__name__)

# When the call is answered, a text is played which prompts the user to press 1 to record the call.
# Once the digit is pressed, the Record API request is made and the recording starts.

@app.route('/record_api/', methods=['POST', 'GET'])
def record_api():

    response = plivoxml.Response()
    getdigits_action_url = url_for('record_action', _external=True)
    getDigits = plivoxml.GetDigits(action=getdigits_action_url,
            method='GET', timeout=7, numDigits=1,
            retries=1, redirect='false')
    getDigits.addSpeak("Press 1 to record this call")
    response.add(getDigits) 
    params = {
        'length' : "10"
    } 
    response.addWait(**params)
    print response.to_xml()
    return Response(str(response), mimetype='text/xml')

# The Record API is invoked by the Get Digits action URL

@app.route('/record_action/', methods=['POST', 'GET'])
def record_action():
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
        }
        response = p.record(params)
    else :
        print "Wrong Input"
    print str(response)
    return Response(str(response), mimetype='text/plain')

if __name__=='__main__':
    app.run(host='0.0.0.0',debug='True')

# Sample successful output
# <Response>
#    <GetDigits action="http://morning-ocean-4669.herokuapp.com/recording_action/" method="GET" numDigits="1" redirect="false" retries="1" timeout="7">
#        <Speak>Press 1 to record this call</Speak>
#    </GetDigits>
#    <Wait length="10" />
# </Response>

# Call UUID is : 2a2875b6-9592-11e4-8b35-cd90edc77fa9 
# Digit pressed is : 1 

#(202, {
#        u'url': u'http://s3.amazonaws.com/recordings_2013/67673232-9594-11e4-baad-842b2b17453e.mp3', 
#        u'recording_id': u'16963644-9594-11e4-baad-842b2b17453e', 
#        u'message': u'call recording started', 
#        u'api_id': u'16847e54-9594-11e4-b423-22000ac8a2f8'
#    }
# )
