import plivo, plivoxml
from flask import Flask

auth_id = "Your AUTH_ID"
auth_token = "Your AUTH_TOKEN"

p = plivo.RestAPI(auth_id, auth_token)

# Machine detection using Call API

params = {
    'to': '1111111111', # The phone numer to which the all has to be placed
    'from' : '2222222222', # The phone number to be used as the caller id
    'answer_url' : "http://morning-ocean-4669.herokuapp.com/detect/", # The URL invoked by Plivo when the outbound call is answered
    'answer_method' : "GET", # Method to invoke the answer_url
    'machine_detection' : "true", # Used to detect if the call has been answered by a machine. The valid values are true and hangup.
    'machine_detection_time' : "10000", # Time allotted to analyze if the call has been answered by a machine. The default value is 5000 ms.
    'machine_detection_url' : "http://morning-ocean-4669.herokuapp.com/machine_detection/", # A URL where machine detection parameters will be sent by Plivo.
    'machine_detection_method' : "GET" # Method used to invoke machine_detection_url
}

# Make an outbound call
response = p.make_call(params)
print str(response)

# Sample Output
# (201, {
#        u'message': u'call fired', 
#        u'request_uuid': u'a52a7ae0-0551-462c-9cf0-1f79f79737c8', 
#        u'api_id': u'45305402-959f-11e4-b932-22000ac50fac'
#    }
# )

# Machine Detection URL example

@app.route('/machine_detection/',methods=['POST', 'GET'])
def machine_detection():
    from_number = request.args.get('From') # The From number which is used to make the call.
    machine = request.args.get('Machine') # This parameter will be true if a machine has been detected on the call.
    to_number = request.args.get('To') # The number which is being called.
    call_uuid = request.args.get('CallUUID') # The ID of the call.
    event = request.args.get('Event') # The event of the notification. This parameter will always have the value MachineDetection.
    call_status = request.args.get('CallStatus') # The status of the call. This will hold the value of in-progress.

    print "From : %s " % (from_number)
    print "To : %s " % (to_number)
    print "Machine : %s " % (machine)
    print "Call UUID : %s " % (call_uuid)
    print "Event : %s " % (event)
    print "Call Status : %s " % (call_status)
    return "OK"

# Sample Output
# From : 2222222222 
# To : 1111111111 
# Machine : true 
# Call UUID : 45704ba2-959f-11e4-802f-e9b058eeb9e5 
# Event : MachineDetection 
# Call Status : in-progress

# As soon as the voicemail finishes speaking, and there is a silence for minSilence milliseconds, 
# the next element in the XML is processed, without waiting for the whole period of length seconds to pass

@app.route('/detect/', methods=['GET','POST'])
def detect():
    try:
        r = plivoxml.Response()
        params = {
            'length': "1000", # Time to wait in seconds
            'silence' : "true", # When silence is set to true, if no voice or sound is detected for minSilence milliseconds, end the wait and continue to the next element in the XML immediately 
            'minSilence' : "3000" # Only used when silence is set to true. The minimum length in milliseconds of silence that needs to be present to qualify as silence
        }
        r.addWait(**params)
        r.addSpeak("Hello Voicemail!")
        print r.to_xml()
        return Response(str(r), mimetype='text/xml')
    except Exception as e:
        print '\n'.join(traceback.format_exc().splitlines())

# Sample Wait XML
# <Response>
#    <Wait length="10" silence="true" minSilence="500"/>
#    <Speak>Hello Voicemail!</Speak>
# </Response>

