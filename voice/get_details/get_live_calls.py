import plivo, plivoxml

auth_id = "Your AUTH_ID"
auth_token = "Your AUTH_TOKEN"

p = plivo.RestAPI(auth_id, auth_token)

params = {
    'status': "live" # The status of the call
}

# Get all live calls
response = p.get_live_calls(params)
print str(response)

# Sample successful output
# (200, {
#	u'calls': [u'a60f44dc-926f-11e4-82f5-b559cbfe39b9', u'af399206-926f-11e4-8b6f-fd067af138be'], 
#	u'api_id': u'23c60a0e-9028-11e4-b423-22000ac8a2f8'
#	}
# )

# Looping through the call uuids

for uuid in response[1]['calls']:
    print uuid

# Sample successful output
# a60f44dc-926f-11e4-82f5-b559cbfe39b9
# af399206-926f-11e4-8b6f-fd067af138be
