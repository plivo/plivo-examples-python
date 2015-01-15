import plivo, plivoxml

auth_id = "Your AUTH_ID"
auth_token = "Your AUTH_TOKEN"

p = plivo.RestAPI(auth_id, auth_token)

params = {
    'call_uuid': '55309cee-821d-11e4-9a73-498d468c930b' # The ID of the call
}

response = p.get_cdr(params)
print str(response)

# Sample successful output
# (200, {
#	u'bill_duration': 0, 
#	u'billed_duration': 0, 
#	u'total_amount': u'0.00000', 
#	u'parent_call_uuid': None, 
#	u'call_direction': u'outbound', 
#	u'call_duration': 0, 
#	u'to_number': u'2222222222', 
#	u'total_rate': u'0.00000', 
#	u'api_id': u'fba71e98-901b-11e4-a2d1-22000ac5040c', 
#	u'from_number': None, 
#	u'end_time': u'2014-12-12 20:39:02+04:00', 
#	u'call_uuid': u'55309cee-821d-11e4-9a73-498d468c930b', 
#	u'resource_uri': u'/v1/Account/XXXXXXXXXXXX/Call/55309cee-821d-11e4-9a73-498d468c930b/'
#	}
# )