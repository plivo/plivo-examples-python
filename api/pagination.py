import plivo,plivoxml

auth_id = "Your AUTH_ID"
auth_token = "Your AUTH_TOKEN"

p = plivo.RestAPI(auth_id, auth_token)

# This example shows how to traverse the list of all applications. 

# Get details all existing applications
params = {
	'limit' : '2', # The number of results per page
	'offset' : '0' # The number of value items by which the results should be offset
}

response = p.get_applications(params)
print response[1]

# Sample successful response
# {
#	u'meta': {
#		u'previous': None, 
#		u'total_count': 12, 
#		u'offset': 0, 
#		u'limit': 2, 
#		u'next': u'/v1/Account/xxxxxxxxxxxxxxxxx/Application/?limit=2&offset=2'
#	}, 	
#	u'objects': [
#		{
#			u'fallback_method': u'POST', 
#			u'default_app': False, 
#			u'app_name': u'Testing_App10', 
#			u'sub_account': None, 
#			u'production_app': False, 
#			u'enabled': True, 
#			u'app_id': u'14344967555248312', 
#			u'public_uri': False, 
#			u'hangup_url': u'http://example.com', 
#			u'sip_uri': u'sip:14344967555248312@app.plivo.com', 
#			u'default_endpoint_app': False, 
#			u'answer_url': u'http://example.com', 
#			u'message_url': u'', 
#			u'resource_uri': u'/v1/Account/XXXXXXXXXXXX/Application/14344967555248312/', 
#			u'hangup_method': u'POST', 
#			u'message_method': u'POST', 
#			u'fallback_answer_url': u'', 
#			u'answer_method': u'POST'
#		}, 
#		{
#			u'fallback_method': u'POST', 
#			u'default_app': False, 
#			u'app_name': u'Testing_App7', 
#			u'sub_account': None, 
#			u'production_app': False, 
#			u'enabled': True, 
#			u'app_id': u'12933174623656681', 
#			u'public_uri': False, 
#			u'hangup_url': u'http://example.com', 
#			u'sip_uri': u'sip:12933174623656681@app.plivo.com', 
#			u'default_endpoint_app': False, 
#			u'answer_url': u'http://example.com', 
#			u'message_url': u'', 
#			u'resource_uri': u'/v1/Account/XXXXXXXXXXXX/Application/12933174623656681/', 
#			u'hangup_method': u'POST', 
#			u'message_method': u'POST', 
#			u'fallback_answer_url': u'', 
#			u'answer_method': u'POST'
#		}
#	], 
#	u'api_id': u'92150f80-8f58-11e4-96e3-22000abcb9af'
# }

# Print the link to view the next page of results
print response[1]['meta']['next']

# Sample successful output
# /v1/Account/XXXXXXXXXXXX/Application/?limit=2&offset=2
# Browse https://api.plivo.com/v1/Account/XXXXXXXXXXXX/Application/?limit=2&offset=2
# to view the next page of results. To traverse pages, browse the 'next' and 'previous' urls