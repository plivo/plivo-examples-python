import plivo,plivoxml

auth_id = "Your AUTH_ID"
auth_token = "Your AUTH_TOKEN"

p = plivo.RestAPI(auth_id, auth_token)

# Create an Endpoint
params = {
    'username': 'testuser', # The username for the endpoint to be created
    'password': 'test123', # The password for your endpoint username
    'alias': 'Test' # Alias for this endpoint
}

response = p.create_endpoint(params)
print str(response)

# Samplesuccessful output
# (201, {
#       u'username': u'testuser141223061753',
#       u'alias': u'Test',
#       u'message': u'created',
#       u'endpoint_id': u'14608873252694',
#       u'api_id': u'6de230bc-8a6b-11e4-ac1f-22000ac51de6'
#       }
# )


# Get details of all existing endpoints
params = {
        'limit': '10', # The number of results per page
        'offset': '0' # The number of value items by which the results should be offset
}

response = p.get_endpoints(params)
print str(response)

# Sample successful output
# (200, {
#       u'meta': {
#               u'previous': None,
#               u'total_count': 7,
#               u'offset': 0,
#               u'limit': 10,
#               u'next': None
#       },
#       u'objects': [
#               {
#                       u'username': u'testuser141223061753',
#                       u'application': u'/v1/Account/xxxxxxxxxxxxxxxxx/Application/16632742496743552/',
#                       u'sip_registered': u'false',
#                       u'sip_uri': u'sip:testuser141223061753@phone.plivo.com',
#                       u'alias': u'Test',
#                       u'endpoint_id': u'14608873252694',
#                       u'password': u'cc03e747a6afbbcbf8be7668acfebee5',
#                       u'sub_account': None,
#                       u'resource_uri': u'/v1/Account/xxxxxxxxxxxxxxxxx/Endpoint/14608873252694/'
#               },
#               {
#                       u'username': u'testuser141218101424',
#                       u'application': u'/v1/Account/xxxxxxxxxxxxxxxxx/Application/16632742496743552/',
#                       u'sip_registered': u'false',
#                       u'sip_uri': u'sip:testuser141218101424@phone.plivo.com',
#                       u'alias': u'Test',
#                       u'endpoint_id': u'21784177241578',
#                       u'password': u'cc03e747a6afbbcbf8be7668acfebee5',
#                       u'sub_account': None,
#                       u'resource_uri': u'/v1/Account/xxxxxxxxxxxxxxxxx/Endpoint/21784177241578/'
#               }
#       ]
# )

# Print the total number of apps
print response[1]['meta']['total_count']

# Sample successful output
# 7

# Get details of a single endpoint
params = {
        'endpoint_id': '21784177241578' # ID of the endpoint for which the details have to be retrieved
}

response = p.get_endpoint(params)
print str(response)

# Sample successful output
# (200,
#       {
#               u'username': u'testuser141218101424',
#               u'application': u'/v1/Account/xxxxxxxxxxxxxxxxx/Application/16632742496743552/',
#               u'sip_registered': u'false',
#               u'api_id': u'f419d274-8a6c-11e4-b153-22000abcaa64',
#               u'sip_uri': u'sip:testuser141218101424@phone.plivo.com',
#               u'alias': u'Test',
#               u'endpoint_id': u'21784177241578',
#               u'password': u'cc03e747a6afbbcbf8be7668acfebee5',
#               u'sub_account': None,
#               u'resource_uri': u'/v1/Account/xxxxxxxxxxxxxxxxx/Endpoint/21784177241578/'
#       }
# )

# Modify an endpoint
params = {
        'endpoint_id' : '21784177241578', # ID of the endpoint that has to be modified
        'alias' : 'New_test' # Values that have to be updated
}

response = p.modify_endpoint(params)
print str(response)

# Sample successful output
# (202,
#       {
#               u'message': u'changed',
#               u'api_id': u'424d84ea-8a6d-11e4-a2d1-22000ac5040c'
#       }
# )

# Delete an endpoint
params = {
        'endpoint_id' : '21784177241578' # ID of the endpoint that as to be deleted
}

response = p.delete_endpoint(params)
print str(response)

# Sample successful endpoint
# (204, '')

# Sample unsuccessful output
# (404, {
#		u'api_id': u'b6d258ee-8f64-11e4-b153-22000abcaa64', 
#		u'error': u'not found'
#		}
# )
