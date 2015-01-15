#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, Response, request
import plivoxml

app=Flask(__name__)

@app.route('/response/conference/', methods=['GET','POST'])
def conference():
	response = plivoxml.Response()
	response.addSpeak('You will now be placed into a demo conference. This is brought to you by Plivo. To know more visit us at plivo.com')
	params = {
	'enterSound' : "beep:2", # Used to play a sound when a member enters the conference
	'record' : "true", # Option to record the call
	'action' : "https://morning-ocean-4669.herokuapp.com/response/conf_action/", # URL to which the API can send back parameters
	'method' : "GET", # method to invoke the action Url
	'record' : "true", # Option to record the call 
	'callbackUrl' : "https://morning-ocean-4669.herokuapp.com/response/conf_callback/", # If specified, information is sent back to this URL
	'callbackMethod' : "GET" # Method used to notify callbackUrl
	# For moderated conference
	'startConferenceOnEnter' : "true", # When a member joins the conference with this attribute set to true, the conference is started.
	                                   # If a member joins a conference that has not yet started, with this attribute value set to false, 
	                                   # the member is muted and hears background music until another member joins the conference
	'endConferenceOnExit' : "true" # If a member with this attribute set to true leaves the conference, the conference ends and all 
	                               # other members are automatically removed from the conference. 
	}
	conference_name = "demo" # Conference Room name
	response.addConference(conference_name, **params)
	return Response(str(response), mimetype='text/xml')

# Action URL Example	

@app.route('/response/conf_action/', methods=['GET','POST'])
def conf_action():
    if request.method == 'GET':
        conf_name = request.args.get('ConferenceName')
        conf_uuid = request.args.get('ConferenceUUID')
        conf_mem_id = request.args.get('ConferenceMemberID')
        record_url = request.args.get('RecordUrl')
        record_id = request.args.get('RecordingID')
    elif request.method == 'POST':
        conf_name = request.form.get('ConferenceName')
        conf_uuid = request.form.get('ConferenceUUID')
        conf_mem_id = request.form.get('ConferenceMemberID')
        record_url = request.form.get('RecordUrl')
        record_id = request.form.get('RecordingID')
    response = make_response('OK')
    response.headers['Content-type'] = 'text/plain'
    print "Conference Name : %s " % (conf_name)
    print "Conference UUID : %s " % (conf_uuid)
    print "Conference Member ID : %s " % (conf_mem_id)
    print "Record URL : %s " % (record_url)
    print "Recording ID : %s " % (record_id)
    return response

# Callback URL Example

@app.route('/response/conf_callback/', methods=['GET','POST'])
def conf_callback():
    if request.method == 'GET':
        conf_action = request.args.get('ConferenceAction')
        conf_name = request.args.get('ConferenceName')
        conf_uuid = request.args.get('ConferenceUUID')
        conf_mem_id = request.args.get('ConferenceMemberID')
        call_uuid = request.args.get('CallUUID')
        record_url = request.args.get('RecordUrl')
        record_id = request.args.get('RecordingID')
    elif request.method == 'POST':
        conf_action = request.form.get('ConferenceAction')
        conf_name = request.form.get('ConferenceName')
        conf_uuid = request.form.get('ConferenceUUID')
        conf_mem_id = request.form.get('ConferenceMemberID')
        call_uuid = request.form.get('CallUUID')
        record_url = request.form.get('RecordUrl')
        record_id = request.form.get('RecordingID')
    response = make_response('OK')
    response.headers['Content-type'] = 'text/plain'
    print "Conference Name : %s " % (conf_name)
    print "Conference UUID : %s " % (conf_uuid)
    print "Conference Member ID : %s " % (conf_mem_id)
    print "Record URL : %s " % (record_url)
    print "Recording ID : %s " % (record_id)
    return response

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)

# Sample Conference XML
# <Response>
# <Speak>You will now be placed into a demo conference. This is brought to you by Plivo. To know more visit us at plivo.com</Speak>
#    <Conference action="https://morning-ocean-4669.herokuapp.com/response/conf_action/" callbackMethod="GET" 
#        callbackUrl="https://morning-ocean-4669.herokuapp.com/response/conf_callback/" enterSound="beep:2" method="GET" record="true" 
#        startConferenceOnEnter="true" endConferenceOnExit="true">demo
#    </Conference>
# </Response>

# Sample output for action URL
# Conference Name : demo
# Conference UUID : 1edcce24-94a6-11e4-a29c-498d468c930b
# Conference Member ID : 4387
# Record URL : http://s3.amazonaws.com/recordings_2000/00000000-1111-2222-3333-4444b5555684.mp3
# Recording ID : 1e9eca52-94a6-11e4-b499-0026b92f9684

# Sample output for Callback URL

# Conference Action : enter
# Conference Name : demo
# Conference UUID : 1edcce24-94a6-11e4-a29c-498d468c930b
# Conference Member ID : 4387
# Call UUID : a59bc002-94a9-11e4-ad11-3f7813869e0a
# Record URL : http://s3.amazonaws.com/recordings_2000/00000000-1111-2222-3333-4444b5555684.mp3
# Recording ID : 1e9eca52-94a6-11e4-b499-0026b92f9684