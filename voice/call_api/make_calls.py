import plivo, plivoxml

auth_id = "Your AUTH_ID"
auth_token = "Your AUTH_TOKEN"

p = plivo.RestAPI(auth_id, auth_token)

params = {
    'to': '2222222222', # The phone numer to which the all has to be placed
    'from' : '1111111111', # The phone number to be used as the caller id
    'answer_url' : "http://morning-ocean-4669.herokuapp.com/speech/", # The URL invoked by Plivo when the outbound call is answered
    'answer_method' : "GET", # The method used to call the answer_url
    # Example for Asynchrnous request
    'callback_url' : "ttp://morning-ocean-4669.herokuapp.com/callback/", # The URL notified by the API response is available and to which the response is sent.
    'callback_method' : "GET" # The method used to notify the callback_url.
}

# Make an outbound call
response = p.make_call(params)

print str(response) 

# Sample successful output for Synchronous Request
# (201, {
#	u'message': u'call fired', 
#	u'request_uuid': u'85b1d45d-bc12-47f5-89c7-ae4a2c5d5713', 
#	u'api_id': u'ad0e27a8-9008-11e4-b932-22000ac50fac'
#	}
# )

# Sample successful output for Asynchronous Request
# (201, {
#   u'message': u'async api spawned',
#   u'api_id': u'ad0e27a8-9008-11e4-b932-22000ac50fac'
#	}
# )
