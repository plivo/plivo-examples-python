import plivo, plivoxml

auth_id = "Your AUTH_ID"
auth_token = "Your AUTH_TOKEN"

p = plivo.RestAPI(auth_id, auth_token)

params = {
    'call_uuid': 'defb0706-86a6-11e4-b303-498d468c930b' # UUID of the call to be hung up
}    

# Hang up a call
response = p.hangup_call(params)
print str(response) 

# Sample successful output
# (204,'')

# Sample unsuccesful output
# (404, {
#	u'api_id': u'790ca696-9012-11e4-b932-22000ac50fac', 
#	u'error': u'call not found'
#	}
# )