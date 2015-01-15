import plivo

auth_id = "Your AUTH_ID"
auth_token = "Your AUTH_TOKEN"

p = plivo.RestAPI(auth_id, auth_token)

# Link an application to a number
params = {
        'number' : '12143010249', # Number that has to be linked to an application
        'app_id' : '16638156474000802' # Application ID that has to be linked
}

response = p.link_application_number(params)
print str(response)

# Sample successful output
# (202, {
#       u'message': u'changed',
#       u'api_id': u'4b342d2e-8a91-11e4-96e3-22000abcb9af'
#       }
# )

# Unlink an application from an number
params = {
        'number' : '12143010249' # Number that has to be unlikned to an application
}

response = p.unlink_application_number(params)
print str(response)

# Sample successful output
# (202, {
#       u'message': u'changed',
#       u'api_id': u'6b70316e-8a91-11e4-a2d1-22000ac5040c'
#       }
# )
