import plivo

auth_id = "Your AUTH_ID"
auth_token = "Your AUTH_TOKEN"

p = plivo.RestAPI(auth_id, auth_token)

# Get all numbers

params = {
	'limit' : '10',
	'offset' : '0'
}
response = p.get_numbers()
print str(response)

# Sample successful output
# (200, {
#	u'meta': {
#		u'previous': None, 
#		u'total_count': 2, 
#		u'offset': 0, 
#		u'limit': 20, 
#		u'next': None
#	}, 
#	u'objects': [
#		{
#			u'voice_enabled': True, 
#			u'application': None, 
#			u'region': u'California, UNITED STATES', 
#			u'number': u'1111111111', 
#			u'sub_account': None, 	
#			u'alias': u'', 
#			u'monthly_rental_rate': u'0.80000', 
#			u'carrier': u'Plivo', 
#			u'sms_rate': u'0.00000', 
#			u'number_type': u'local', 
#			u'voice_rate': u'0.00850', 
#			u'sms_enabled': True, 
#			u'added_on': u'2014-10-28', 
#			u'resource_uri': u'/v1/Account/XXXXXXXXXXXX/Number/18583650866/'
#		}, 
#		{
#			u'voice_enabled': True, 
#			u'application': u'/v1/Account/XXXXXXXXXXXX/Application/26469261154421101/', 
#			u'region': u'UNITED KINGDOM', 
#			u'number': u'4444444444', 
#			u'sub_account': None, 
#			u'alias': None, 
#			u'monthly_rental_rate': u'0.80000', 
#			u'carrier': u'Plivo', 
#			u'sms_rate': u'0.00000', 
#			u'number_type': u'local', 
#			u'voice_rate': u'0.00500', 
#			u'sms_enabled': True, 
#			u'added_on': u'2014-12-04', 
#			u'resource_uri': u'/v1/Account/XXXXXXXXXXXX/Number/447441906862/'
#		}
#	], 
#	u'api_id': u'c51cd630-8a8d-11e4-b153-22000abcaa64'
#	}
# )

# Get a particular number
params = {
	'number' : '1111111111' # PHone number for which the details have to be retrieved
}

response = p.get_number(params)
print str(response)

# Sample successful output
# (200, {
#	u'voice_enabled': True, 
#	u'application': u'/v1/Account/XXXXXXXXXXXX/Application/26469261154421101/', 
#	u'region': u'UNITED KINGDOM', 
#	u'number': u'4444444444', 
#	u'api_id': u'855ad4b0-8a8e-11e4-b153-22000abcaa64', 
#	u'sub_account': None, 
#	u'alias': None, 
#	u'monthly_rental_rate': u'0.80000', 
#	u'carrier': u'Plivo', 
#	u'sms_rate': u'0.00000', 
#	u'number_type': u'local', 
#	u'voice_rate': u'0.00500', 
#	u'sms_enabled': True, 
#	u'added_on': u'2014-12-04', 
#	u'resource_uri': u'/v1/Account/XXXXXXXXXXXX/Number/447441906862/'
#	}
# )

