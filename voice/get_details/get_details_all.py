import plivo, plivoxml

auth_id = "Your AUTH_ID"
auth_token = "Your AUTH_TOKEN"

p = plivo.RestAPI(auth_id, auth_token)

response = p.get_cdrs()

# Prints the complete response
print str(response)	

# Sample successful output
# (200, {
#	u'meta': {
#		u'previous': None, 
#		u'total_count': 37, 
#		u'offset': 0, 
#		u'limit': 20, 
#		u'next': u'/v1/Account/XXXXXXXXXXXXXXX/Call/?limit=20&offset=20'
#	}, 
#	u'objects': [
#		{
#			u'bill_duration': 0, 
#			u'billed_duration': 0, 
#			u'total_amount': u'0.00000', 
#			u'parent_call_uuid': None, 
#			u'call_direction': u'inbound', 
#			u'call_duration': 0, 
#			u'to_number': u'18583650866', 
#			u'total_rate': u'0.00850', 
#			u'from_number': u'14155069431', 
#			u'end_time': u'2014-12-30 21:56:33+04:00', 
#			u'call_uuid': u'30350d24-904d-11e4-aa47-f91d0b204d04', 
#			u'resource_uri': u'/v1/Account/XXXXXXXXXXXXXXX/Call/30350d24-904d-11e4-aa47-f91d0b204d04/'
#		}, 
#		{
#			u'bill_duration': 0, 
#			u'billed_duration': 0, 
#			u'total_amount': u'0.00000', 
#			u'parent_call_uuid': None, 
#			u'call_direction': u'inbound', 
#			u'call_duration': 0, 
#			u'to_number': u'18583650866', 
#			u'total_rate': u'0.00850', 
#			u'from_number': u'14155069431', 
#			u'end_time': u'2014-12-30 21:54:09+04:00', 
#			u'call_uuid': u'da84966a-904c-11e4-bdae-b559cbfe39b9', 
#			u'resource_uri': u'/v1/Account/XXXXXXXXXXXXXXX/Call/da84966a-904c-11e4-bdae-b559cbfe39b9/'
#		}
#	]
#)	

# Filtering the records

params = {
    'end_time__gt' : "2014-12-23 11:47", # Filter out calls according to the time of completion. gte stands for greater than or equal.
    'call_direction' : "inbound", # Filter the results by call direction. The valid inputs are inbound and outbound
    'from_number' : "1111111111", # Filter the results by the number from where the call originated
    'to_number' : "2222222222", # Filter the results by the number to which the call was made
	'limit' : '10', # The number of results per page
	'offset' : '0' # The number of value items by which the results should be offset
}

response = p.get_cdrs(params)
print str(response)	

# Sample successful output
# (200, {
#	u'meta': {
#		u'previous': None, 
#		u'total_count': 2, 
#		u'offset': 0, 
#		u'limit': 10, 
#		u'next': None
#	}, 
#	u'objects': [
#		{
#			u'bill_duration': 18, 
#			u'billed_duration': 60, 
#			u'total_amount': u'0.00850', 
#			u'parent_call_uuid': None, 
#			u'call_direction': u'inbound', 
#			u'call_duration': 18, 
#			u'to_number': u'18583650866', 
#			u'total_rate': u'0.00850', 
#			u'from_number': u'14155069431', 
#			u'end_time': u'2014-12-30 16:00:50+04:00', 
#			u'call_uuid': u'74430d86-901b-11e4-9a96-71f618784e1e', 
#			u'resource_uri': u'/v1/Account/XXXXXXXXXXXXXXX/Call/74430d86-901b-11e4-9a96-71f618784e1e/'
#		}, 
#		{
#			u'bill_duration': 13, 
#			u'billed_duration': 60, 
#			u'total_amount': u'0.00850', 
#			u'parent_call_uuid': None, 
#			u'call_direction': u'inbound', 
#			u'call_duration': 13, 
#			u'to_number': u'18583650866', 
#			u'total_rate': u'0.00850', 
#			u'from_number': u'14155069431', 
#			u'end_time': u'2014-12-30 15:59:16+04:00', 
#			u'call_uuid': u'3f2192a8-901b-11e4-93ac-c374cdd23d80', 
#			u'resource_uri': u'/v1/Account/XXXXXXXXXXXXXXX/Call/3f2192a8-901b-11e4-93ac-c374cdd23d80/'
#		}
#	]
# )