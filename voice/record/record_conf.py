from flask import Flask, make_response, request
import plivo, plivoxml

app = Flask(__name__)

# Generates a Conference XML

@app.route("/response/conference/", methods=['GET', 'POST'])
def conference():
    response = plivoxml.Response()
    response.addSpeak('You will now be placed into a demo conference.')
    params = {
    'enterSound' : "beep:1", # Used to play a sound when a member enters the conference
    'callbackUrl' : "https://morning-ocean-4669.herokuapp.com/response/conf_callback/", # If specified, information is sent back to this URL
    'callbackMethod' : "GET" # Method used to notify callbackUrl
    }
    conference_name = "demo" # Conference Room name
    response.addConference(conference_name, **params)
    print response.to_xml()
    return Response(str(response), mimetype='text/xml')

# Record API is called in the callback URL to record the conference.

@app.route('/response/conf_callback/', methods=['GET','POST'])
def conf_callback():
    if request.method == 'GET':
        conf_name = request.args.get('ConferenceName')
        event = request.args.get('Event')
    elif request.method == 'POST':
        conf_name = request.form.get('ConferenceName')
        event = request.form.get('Event')
    response = make_response('OK')
    response.headers['Content-type'] = 'text/plain'
    print "Conference Name : %s " % (conf_name)

    # The recording starts when the user enters the conference room
    
    if event == "ConferenceEnter":
        auth_id = "Your AUTH_ID"
        auth_token = "Your AUTH_TOKEN"
        p = plivo.RestAPI(auth_id, auth_token)

        params = {
            'conference_name' : conf_name
        }

        response = p.record_conference(params)
        print str(response)
        return str(response)
    else:
        print "invalid"
        return Response("INVALID", mimetype='text/plain')

# Sample Output
# <Response>
# <Speak>You will now be placed into a demo conference. This is brought to you by Plivo. To know more visit us at plivo.com</Speak>
#    <Conference callbackMethod="GET" callbackUrl="https://morning-ocean-4669.herokuapp.com/response/conf_callback/"
#         enterSound="beep:1">demo
#    </Conference>
# </Response>

# (202, {
#        u'recording_id': u'59f6f012-9644-11e4-8bd4-842b2b16384f', 
#        u'api_id': u'59eaad34-9644-11e4-b423-22000ac8a2f8', 
#        u'url': u'http://s3.amazonaws.com/recordings_2013/34347876-9644-11e4-8bd4-842b2b16384f.mp3', 
#        u'message': u'conference recording started'
#    }
# )
