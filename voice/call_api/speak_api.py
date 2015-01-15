import plivo
from flask import Flask, Response

app = Flask(__name__)

@app.route('/speak_api/', methods=['GET', 'POST'])
def speak_api():

    response = plivoxml.Response()
    getdigits_action_url = url_for('speak_action', _external=True)
    getDigits = plivoxml.GetDigits(action=getdigits_action_url,
            method='GET', timeout=7, numDigits=1,
            retries=1, redirect='false')
    getDigits.addSpeak("Press 1 to listen to a message")
    response.add(getDigits) 
    params = {
        'length' : "10"
    } 
    response.addWait(**params)
    print response.to_xml()
    return Response(str(response), mimetype='text/xml')

@app.route('/speak_action/', methods=['GET', 'POST'])
def speak_action():
    digit = request.args.get('Digits')
    call_uuid = request.args.get('CallUUID')
    auth_id = "Your AUTH_ID"
    auth_token = "Your AUTH_TOKEN"
    print "Call UUID is : %s " % (call_uuid)
    print "Digit pressed is : %s " % (digit)
    p = plivo.RestAPI(auth_id, auth_token)
    if digit == "1":
        params = {
            'call_uuid': call_uuid, # ID of the call
            'text' : "Hello from Speak API", # Text to be played.
            'voice' : "WOMAN", # The voice to be used, can be MAN,WOMAN. Defaults to WOMAN.
            'language' : "en-GB", # The language to be used
        }
        response = p.speak(params)
    else :
        print "Wrong Input"
    print str(response)
    return Response(str(response), mimetype='text/plain') 

if __name__=='__main__':
	app.run(host='0.0.0.0',debug='True')

# Sample successful output
# <Response>
#    <GetDigits action="http://morning-ocean-4669.herokuapp.com/speak_action/" method="GET" numDigits="1" redirect="false" retries="1" timeout="7">
#        <Speak>Press 1 to listen to a message</Speak>
#    </GetDigits>
#    <Wait length="10" />
# </Response>

# Call UUID is : 01d03d86-958f-11e4-a25f-c374cdd23d80 
# Digit pressed is : 1 

# (202, {
#       u'api_id': u'0753c6a6-958f-11e4-ac1f-22000ac51de6', 
#        u'message': u'speak started'
#    }
# )
