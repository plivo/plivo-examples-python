#!/usr/bin/env python
# -*- coding: utf-8 -*-
import plivo

# Your PLIVO_AUTH_ID and PLIVO_AUTH_TOKEN can be found on your Plivo Dashboard https://manage.plivo.com/dashboard

auth_id = "Your AUTH_ID"
auth_token = "Your AUTH_TOKEN"

# Enter your Plivo phone number. This will show up on your caller ID
plivo_number = "1111111111"

# Enter the URL of where your conferenceXML.py file is
answer_url = "https://morning-ocean-4669.herokuapp.com/response/conference/"

# Enter the 3 phone numbers you want to join in on the conference call

# The following format is supported only when bulk calling is enabled: 14155555555<14156666666<14157777777

# Note that this is a delimiter that's specific to Plivo's API
# which allows you to call multiple numbers at the same time
# Check out plivo.com/docs/api/call for more info

p = plivo.RestAPI(auth_id, auth_token)

conference_numbers = ["2222222222", "3333333333"]

call_params = {
    'from': plivo_number, # The phone number to be used as the caller id
    'answer_url': answer_url, # The URL invoked by Plivo when the outbound call is answered
    'answer_method' : "GET" # The method used to call the answer_url
    }

for number in conference_numbers:
    call_params['to'] = number
    r = p.make_call(call_params)
    print str(r)

# Sample successful output
# (201, {
#	u'message': u'call fired', 
#	u'request_uuid': u'3707244b-6285-4c81-9fee-5185eb36695b', 
#	u'api_id': u'51ef99dc-9298-11e4-b153-22000abcaa64'
#	}
# )
#(201, {
#	u'message': u'call fired', 
#	u'request_uuid': u'13031209-d785-4d3e-ab0a-e19aa6aa9633', 
#	u'api_id': u'5340628a-9298-11e4-b932-22000ac50fac'
#	}
# )