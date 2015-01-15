import plivo

auth_id = "Your AUTH_ID"
auth_token = "Your AUTH_TOKEN"

p = plivo.RestAPI(auth_id, auth_token)

# Get account details
response = p.get_account()
print str(response)

# Sample successful output
# (200,
#       {
#               u'city': u'Testing City',
#               u'account_type': u'standard',
#               u'name': u'Abctest',
#               u'cash_credits': u'89.38274',
#               u'state': u'',
#               u'api_id': u'0760deee-8a6e-11e4-a2d1-22000ac5040c',
#               u'billing_mode': u'prepaid',
#               u'auto_recharge': False,
#               u'address': u'Sample address',
#               u'timezone': u'US/Texas',
#               u'auth_id': u'xxxxxxxxxxxxxxxx',
#               u'resource_uri': u'/v1/Account/xxxxxxxxxxxxxxxx/'
#       }
# )

# Modify account
params = {
        'name'  : 'Test' # Name of the account holder or business.
        'city'  : 'Testing City', # City of the account holder
        'address' : 'Sample address', # Address of the account holder
        'timezone' : 'Indian/Mauritius' # Time zone of the account holder
}

response = p.modify_account(params)
print str(response)

# Sample successful output
# (202,
#       {
#               u'message': u'changed',
#               u'api_id': u'a1ce9df4-8a6e-11e4-96e3-22000abcb9af'
#       }
# )

# Create a sub account
params = {
        'name' : 'test_subaccount1', # Name of the subaccount
        'enabled' : 'True' # Specify if the subaccount should be enabled or not
}

response = p.create_subaccount(params)
print str(response)

# Sample successful output
# (201,
#       {
#               u'auth_token': u'YjFhM2EzNWExM2M4NmU3MzNmZGRiMjFiM2M3N2Qz',
#               u'message': u'created',
#               u'auth_id': u'SAM2U3ZDEXOTK0NTMWMJ',
#               u'api_id': u'e549d6b6-8a6e-11e4-96e3-22000abcb9af'
#       }
# )

# Modify a sub account
params = {
        'subauth_id' : 'ZZZZZZZZZZZZ', # Auth ID of the sub acccount that has to be modified
        'name' : 'ABC_test' # Name of the subaccount
}

response = p.modify_subaccount(params)
print str(response)

# Sample successful output
# (202, {
#       u'message': u'changed',
#       u'api_id': u'94a402fc-8a70-11e4-b423-22000ac8a2f8'
#       }
# )

# Get details of all sub accounts
params = {
        'limit' : '5', # The number of results per page
        'offset' : '1' # The number of value items by which the results should be offset
}
response = p.get_subaccounts()
print str(response)

# Sample successful output
#(200, {
#       u'meta': {
#               u'previous': None,
#               u'total_count': 3,
#               u'offset': 0,
#               u'limit': 20,
#               u'next': None
#       },
#       u'objects': [
#               {
#                       u'account': u'/v1/Account/XXXXXXXXXXXXXXXXX/',
#                       u'name': u'test_subaccount1',
#                       u'created': u'2014-12-23',
#                       u'auth_token': u'YYYYYYYYYYYYY',
#                       u'enabled': False,
#                       u'modified': None,
#                       u'new_auth_token': u'YYYYYYYYYYYYY',
#                       u'auth_id': u'ZZZZZZZZZZZZ',
#                       u'resource_uri': u'/v1/Account/XXXXXXXXXXXXXXXXX/Subaccount/ZZZZZZZZZZZZ/'
#               },
#               {
#                       u'account': u'/v1/Account/XXXXXXXXXXXXXXXXX/',
#                       u'name': u'test_subaccount2',
#                       u'created': u'2014-12-19',
#                       u'auth_token': u'YYYYYYYYYYYYY',
#                       u'enabled': False,
#                       u'modified': None,
#                       u'new_auth_token': u'YYYYYYYYYYYYY',
#                       u'auth_id': u'ZZZZZZZZZZZZ',
#                       u'resource_uri': u'/v1/Account/XXXXXXXXXXXXXXXXX/Subaccount/ZZZZZZZZZZZZ/'
#               }
#       ],
#       u'api_id': u'324f3028-8a6f-11e4-a2d1-22000ac5040c'
#       }
# )

# Print the total number of apps
print response[1]['meta']['total_count']

# Sample successful output
# 3

# Get details of a particular sub acount
params = {
        'subauth_id' : 'ZZZZZZZZZZZZ' # Auth ID of the sub acccount for which the details hae to be retrieved
}

response = p.get_subaccount(params)
print str(response)

# Sample successful output
# (200, {
#               u'account': u'/v1/Account/XXXXXXXXXXXXXXXXX/',
#               u'name': u'test_subaccount1',
#               u'created': u'2014-12-23',
#               u'auth_token': u'YYYYYYYYYYYYY',
#               u'enabled': False,
#               u'modified': None,
#               u'api_id': u'31b185ca-8a70-11e4-b932-22000ac50fac',
#               u'new_auth_token': u'YYYYYYYYYYYYY',
#               u'auth_id': u'ZZZZZZZZZZZZ',
#               u'resource_uri': u'/v1/Account/XXXXXXXXXXXXXXXXX/Subaccount/ZZZZZZZZZZZZ/'
#       }
# )

# Delete a sub account
params = {
        'subauth_id' : 'ZZZZZZZZZZZZ' # Auth ID of the sub acccount that has to be deleted
}

response = p.delete_subaccount(params)
print str(response)

# Sample successful output
# (204, '')

# Sample unsuccessful output
# (404, {
#       u'api_id': u'28eb91a2-8f65-11e4-a2d1-22000ac5040c', 
#       u'error': u'not found'
#       }
# )
