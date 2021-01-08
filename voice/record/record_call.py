from flask import Flask, make_response, request, Response
from plivo import plivoxml

app = Flask(__name__)

@app.route('/record/',methods=['POST', 'GET'])
def record():

    # Generate a Record XML and ask the caller to leave
    # a message.

    # The recorded file will be sent to the 'action' URL
    response = plivoxml.ResponseElement()
    response.add(
    plivoxml.RecordElement(
        action="http://foo.com/record_action/",  # Submit the result of the record to this URL
        method="GET",  # HTTP method to submit the action URL
        callback_url="https://www.foo.com/record_callback/",  # If set, this URL is fired in background when the recorded file is ready to be used.
        callback_method="GET",  # Method used to notify the callbackUrl.
    )
    )
    return Response(response.to_string(), mimetype="application/xml")


# Action URL Example

@app.route('/record_action/',methods=['POST', 'GET'])
def record_action():
    record_url = request.form.get('RecordUrl')
    record_duration = request.form.get('RecordingDuration')
    record_id = request.form.get('RecordingID')
    response = make_response('OK')
    response.headers['Content-type'] = 'text/plain'
    print ("Record URL : %s " % (record_url))
    print ("Recording Duration : %s " % (record_duration))
    print ("Recording ID : %s " % (record_id))
    return response

# Callback URL Example

@app.route('/record_callback/',methods=['POST', 'GET'])
def record_callback():
    record_url = request.form.get('RecordUrl')
    record_duration = request.form.get('RecordingDuration')
    record_id = request.form.get('RecordingID')
    response = make_response('OK')
    response.headers['Content-type'] = 'text/plain'
    print("Record URL : %s " % (record_url))
    print("Recording Duration : %s " % (record_duration))
    print("Recording ID : %s " % (record_id))
    return response

# Sample output for Record XML
# <Response>
#   <Record action="http://foo.com/record_action/" method="GET" callbackUrl="https://www.foo.com/record_callback/" callbackMethod="GET"/>
# </Response>


# Sample output for Action URL
# Record URL : http://s3.amazonaws.com/recordings_2013/11111111-5555-6666-2222-999944421718.mp3 
# Recording Duration : 8 
# Recording ID : a34d252c-94b1-11e4-ab5e-842b2b021718

# Sample output for Callback URL
# Record URL : http://s3.amazonaws.com/recordings_2013/11111111-5555-6666-2222-999944421718.mp3 
# Recording Duration : 8 
# Recording ID : a34d252c-94b1-11e4-ab5e-842b2b021718
