import plivo,plivoxml
from flask import Flask, Response, request
import traceback

app = Flask(__name__)

# A call is made to the plivo number. 
# The answer_url returns and XML that starts recording the session and then dials to another number.
# When the user pick up, the B Leg record starts and a music is played.

# The action URL of the Record tag will return the Session recording details

@app.route('/answer_incoming/', methods=['GET','POST'])
def answer_incoming():
    r = plivoxml.Response()
    record_params = {
        'action' : "https://morning-ocean-4669.herokuapp.com/record_action/",
        'method' : "GET",
        'redirect' : "false",
        'recordSession' : "true"
    }
    r.addRecord(**record_params)
    wait_params = {
        'length' : "5"
    }
    r.addWait(**wait_params)
    r.addSpeak("Connecting your call!")
    dial_params = {
        'callbackUrl' : "https://morning-ocean-4669.herokuapp.com/dial_outbound/",
        'callbackMethod' : "GET"
    }
    d = r.addDial(**dial_params)
    d.addNumber("1111111111")
    print r.to_xml()
    return Response(str(r), mimetype='text/xml')

# The Callback URL of Dial will make a request to the Record API which will record only the B Leg
# Play API is invoked which will play a music only on the B Leg.

@app.route('/dial_outbound/', methods=['GET','POST'])
def dial_outbound():
    try:
        event = request.args.get('Event')
        call_uuid = request.args.get('DialBLegUUID')
        if event == "DialAnswer":
            auth_id = "Your AUTH_ID"
            auth_token = "Your AUTH_TOKEN"
            p = plivo.RestAPI(auth_id, auth_token)
            record_params = {
                'call_uuid' : call_uuid,
                'callback_url' : "https://morning-ocean-4669.herokuapp.com/recording_callback/",
                'callback_method' : "GET"
            }
            response = p.record(record_params)
            print str(response)
            play_params = {
                'call_uuid' : call_uuid,
                'urls' : "https://s3.amazonaws.com/plivocloud/Trumpet.mp3"
            }
            response = p.play(play_params)
            print str(response)
            return Response(response, mimetype='text/plain')
        else:
            print "Invalid"
            return Response("INVALID", mimetype='text/plain')
    except Exception as e:
        print '\n'.join(traceback.format_exc().splitlines())

# The Callback URL of record api will return the B Leg record details.

@app.route('/recording_callback/', methods=['GET','POST'])
def recording_callback():
    if request.method == 'GET':
        record_url = request.args.get('record_url')
        record_duration = request.args.get('recording_duration')
        record_id = request.args.get('recording_id')
    elif request.method == 'POST':
        record_url = request.form.get('record_url')
        record_duration = request.form.get('recording_duration')
        record_id = request.form.get('recording_id')
    response = make_response('OK')
    response.headers['Content-type'] = 'text/plain'
    print "Record URL : %s " % (record_url)
    print "Recording Duration : %s " % (record_duration)
    print "Recording ID : %s " % (record_id)
    return response    

if __name__=='__main__':
    app.run(host='0.0.0.0',debug='True')  

# Sample Output
# <Response>
#    <Record action="https://morning-ocean-4669.herokuapp.com/record_action/" callbackMethod="GET" callbackUrl="https://morning-ocean-4669.herokuapp.com/record_action/" 
#        method="GET" recordSession="true" redirect="false" />
#    <Wait length="5" />
#    <Speak>Connecting your call!</Speak>
#    <Dial callbackMethod="GET" callbackUrl="https://morning-ocean-4669.herokuapp.com/dial_outbound/">
#        <Number>1111111111</Number>
#    </Dial>
# </Response>

# Output from the Record XML action URL
# Record URL : http://s3.amazonaws.com/recordings_2013/55556666-7777-11e4-a4c8-782bcb5bb8af.mp3 
# Recording Duration : -1 
# Recording ID : daddbf04-9585-11e4-a4c8-782bcb5bb8af 

# Output of the Record API request
# (200, {
#        u'message': u'async api spawned', 
#        u'api_id': u'e3403906-9585-11e4-b153-22000abcaa64'
#    }
# )

# Output of the Play XML request
# (202, {
#        u'message': u'play started', 
#        u'api_id': u'e3791dca-9585-11e4-96e3-22000abcb9af'
#    }
# )

# Output of Record API Callback URL
# Record URL : http://s3.amazonaws.com/recordings_2013/11112222-4444-11e4-a4c8-782bcb5bb8af.mp3
# Recording Duration : 22 
# Recording ID : 693e61fd-8150-4091-a0f8-561d4a434288 

# Output of Record XML Callback URL
# Record URL : http://s3.amazonaws.com/recordings_2013/55556666-7777-11e4-a4c8-782bcb5bb8af.mp3 
# Recording Duration : 27 
# Recording ID : daddbf04-9585-11e4-a4c8-782bcb5bb8af 



