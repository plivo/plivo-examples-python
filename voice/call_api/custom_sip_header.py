import plivo, plivoxml

auth_id = "Your AUTH_ID"
auth_token = "Your AUTH_TOKEN"

p = plivo.RestAPI(auth_id, auth_token)

# API ID is returned for every API request. 
# Request UUID is request id of the call. This ID is returned as soon as the call is fired irrespective of whether the call is answered or not

params = {
    'to': 'sip:abcd150105094929@phone.plivo.com', # The phone numer to which the all has to be placed. Sip endpoints must be prefixed with sip:
    'from' : '1111111111', # The phone number to be used as the caller id
    'answer_url' : "http://morning-ocean-4669.herokuapp.com/speech/", # The URL invoked by Plivo when the outbound call is answered
    'answer_method' : "GET", # Method to invoke the answer_url
    'sip_headers' : "Test=Sample" # List of SIP headers in the form of 'key=value' pairs, separated by commas.
}

# Make an outbound call
response = p.make_call(params)
print str(response)

# Sample Output
# (201, {
#       u'message': u'call fired', 
#       u'request_uuid': u'08a363f2-5af6-4ee3-aa47-8966881fae13', 
#       u'api_id': u'fd255c14-958c-11e4-a2d1-22000ac5040c'
#    }
# )

# The SIP header can be seen as a query parameter in the answer_url
# path="/speech/?Direction=outbound&From=1111111111&ALegUUID=5260e820-958c-11e4-b6bf-498d468c930b&BillRate=0.00300&
# To=sip%3Aabcd150105094929%40phone.plivo.com&X-PH-Test=Sample&CallUUID=5260e820-958c-11e4-b6bf-498d468c930b&ALegRequestUUID=2202d0ab-a890-4199-8582-e7a2615cb23b&
# RequestUUID=2202d0ab-a890-4199-8582-e7a2615cb23b&SIP-H-To=%3Csip%3Aabcd150105094929%40phone.plivo.com%3E%3Btag%3D6U9J4.uVHI7KyEKSgD8vrPnAKQoR2QXc&
# CallStatus=in-progress&Event=StartApp" host=morning-ocean-4669.herokuapp.com request_id=07c4ae01-65d6-4463-afcd-ebdd9f6812e0 fwd="54.241.2.243" 
# dyno=web.1 connect=2ms service=5ms status=200 bytes=1104
