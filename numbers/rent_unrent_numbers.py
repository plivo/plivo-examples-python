import plivo

auth_id = "Your AUTH_ID"
auth_token = "Your AUTH_TOKEN"

p = plivo.RestAPI(auth_id, auth_token)

# Rent a number
params = {
        'group_id' : '86930523496041' # The ID associated with a particular prefix for a number
}
response = p.rent_from_number_group(params)
print str(response)

# Sample successful output
# (201, {
#       u'status': u'fulfilled',
#       u'message': u'created',
#       u'numbers': [
#               {
#                       u'status': u'Success',
#                       u'number': u'12143010272'
#               }
#       ],
#       u'api_id': u'8987963e-8a90-11e4-b423-22000ac8a2f8'
#       }
# )

# Modify alias of a number
params = {
        'number' : '12143010249', # Number that has to be modified
        'alias' : 'testing' # The textual name given to the number
}

response = p.modify_number(params)
print str(response)

# Sample successful output
# (202, {
#       u'message': u'changed',
#       u'api_id': u'e13fcf9a-8a90-11e4-b423-22000ac8a2f8'
#       }
# )

# Modify the application linked to a number
params = {
        'number' : '12143010249', # Number that has to be modified
        'app_id' : '16638156474000802' # The application id of the application that is to be linked
}

response = p.modify_number(params)
print str(response)

# Sample successful output
# (202, {
#		u'message': u'changed', 
#		u'api_id': u'e78761bc-8f52-11e4-b423-22000ac8a2f8'
#		}
# )

# Unrent a number
params = {
        'number' : '12143010249' # Number that has to be unrented
}

response = p.unrent_number(params)
print str(response)

# Sample successful output
# (204, '')

# Sample unsuccessful output
# (404, {
#		u'api_id': u'7c33ff78-8f53-11e4-b932-22000ac50fac', 
#		u'error': u'not found'
#		}
# )	
