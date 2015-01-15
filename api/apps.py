import plivo,plivoxml

auth_id = "Your AUTH_ID"
auth_token = "Your AUTH_TOKEN"

p = plivo.RestAPI(auth_id, auth_token)

# Create a new application
params = {
    'answer_url': 'http://example.com', # The URL Plivo will fetch when a call executes this application
    'app_name': 'Testing_App' # The name of your application
}

response = p.create_application(params)
print str(response)

# Sample successful output
# (201, {
#       u'message': u'created',
#       u'app_id': u'21935628481970026',
#       u'api_id': u'a50543a6-8a64-11e4-b153-22000abcaa64'
#       }
# )

# Get details all existing applications
params = {
        'limit' : '10', # The number of results per page
        'offset' : '0' # The number of value items by which the results should be offset
}

response = p.get_applications(params)
print str(response)

# Sample successful output
#(200, {
#       u'meta': {
#               u'previous': None,
#               u'total_count': 7,
#               u'offset': 0,
#               u'limit': 10,
#               u'next': None
#       },
#       u'objects': [
#               {
#                       u'fallback_method': u'POST',
#                       u'default_app': False,
#                       u'app_name': u'Testing_App',
#                       u'sub_account': None,
#                       u'production_app': False,
#                       u'enabled': True,
#                       u'app_id': u'21935628481970026',
#                       u'public_uri': False,
#                       u'hangup_url': u'http://example.com',
#                       u'sip_uri': u'sip:21935628481970026@app.plivo.com',
#                       u'default_endpoint_app': False,
#                       u'answer_url': u'http://example.com',
#                       u'message_url': u'',
#                       u'resource_uri': u'/v1/Account/xxxxxxxxxxxxxxxxx/Application/21935628481970026/',
#                       u'hangup_method': u'POST',
#                       u'message_method': u'POST',
#                       u'fallback_answer_url': u'',
#                       u'answer_method': u'POST'
#               },
#               {
#                       u'fallback_method': u'POST',
#                       u'default_app': False,
#                       u'app_name': u'Receive SMS',
#                       u'sub_account': None,
#                       u'production_app': False,
#                       u'enabled': True,
#                       u'app_id': u'26469261154421101',
#                       u'public_uri': False,
#                       u'hangup_url': u'http://morning-ocean-4669.herokuapp.com/response/conference/',
#                       u'sip_uri': u'sip:26469261154421101@app.plivo.com',
#                       u'default_endpoint_app': False,
#                       u'answer_url': u'http://morning-ocean-4669.herokuapp.com/response/conference/',
#                       u'message_url': u'http://morning-ocean-4669.herokuapp.com/message/',
#                       u'resource_uri': u'/v1/Account/xxxxxxxxxxxxxxxxx/Application/26469261154421101/',
#                       u'hangup_method': u'POST',
#                       u'message_method': u'GET',
#                       u'fallback_answer_url': u'',
#                       u'answer_method': u'GET'
#               }
#       ]
# )

# Print the total number of apps
print response[1]['meta']['total_count']

# Sample successful output
# 6

# Print public_uri, default_app, default_endpoint
for i in range(0,response[1]['meta']['total_count']):
    print "public_uri : %s" % (response[1]['objects'][i]['public_uri'])
    print "default_app : %s" % (response[1]['objects'][i]['default_app'])
    print "default_endpoint_app : %s" % (response[1]['objects'][i]['default_endpoint_app'])

# Get details of a single application
params = {
        'app_id': '16631550192125875' # ID of the application for which the details have to be retrieved
}

response = p.get_application(params)
print str(response)

# Sample successful output
#(200,
#       {
#               u'fallback_method': u'GET',
#               u'default_app': True,
#               u'app_name': u'Phone TTS',
#               u'sub_account': None,
#               u'production_app': False,
#               u'enabled': True,
#               u'app_id': u'16631550192125875',
#               u'api_id': u'e90bca98-8a69-11e4-ac1f-22000ac51de6',
#               u'hangup_url': u'http://mysterious-reaches-5041.herokuapp.com/response/speak/',
#               u'sip_uri': u'sip:16631550192125875@app.plivo.com',
#               u'default_endpoint_app': False,
#               u'answer_url': u'https://morning-ocean-4669.herokuapp.com/speech/',
#               u'public_uri': False,
#               u'message_url': u'https://morning-ocean-4669.herokuapp.com/response/conference/',
#               u'resource_uri': u'/v1/Account/xxxxxxxxxxxxxxxxx/Application/16631550192125875/',
#               u'hangup_method': u'POST',
#               u'message_method': u'POST',
#               u'fallback_answer_url': u'',
#               u'answer_method': u'GET'
#       }
#)

# Modify an application

params = {
        'app_id' : '16631550192125875', # ID of the application that has to be modified
        'answer_url': 'http://exampletest.com' # Values that have to be updated
}

response = p.modify_application(params)
print str(response)

# Sample successful output
# (202, {
#       u'message': u'changed',
#       u'api_id': u'6d886ed4-8a6a-11e4-ac1f-22000ac51de6'
#       }
# )

# Delete an application
params = {
        'app_id' : '16631550192125875' # ID of the application that as to be deleted
}
response = p.delete_application(params)
print str(response)

# Sample successful output
# (204, '')

# Sample unsuccessful output
# (404, {
#       u'api_id': u'5fbdd916-8f64-11e4-b153-22000abcaa64', 
#       u'error': u'not found'
#       }
# )