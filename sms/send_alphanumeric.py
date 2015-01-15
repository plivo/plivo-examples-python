import plivo

auth_id = "Your AUTH_ID"
auth_token = "Your Auth_TOKEN"

p = plivo.RestAPI(auth_id, auth_token)

params = {
    'src': 'TEST', # Alphanumeric sender ID
    'dst' : '1111111111', # Receiver's phone number with ountry code
    'text' : "Hi, from Plivo" # Your SMS text message
}

response = p.send_message(params)

# Prints the complete response
print str(response)

# Sample successful output
# (202, {
#               u'message': u'message(s) queued',
#               u'message_uuid': [u'53e6526a-8a7a-11e4-a77d-22000ae383ea'],
#               u'api_id': u'53cc4532-8a7a-11e4-96e3-22000abcb9af'
#       }
# )

# Prints only the status code
print response[0]

# Sample successful output
# 202

# Prints the message details
print response[1]

# Sample successful output
# {
#       u'message': u'message(s) queued',
#       u'message_uuid': [u'53e6526a-8a7a-11e4-a77d-22000ae383ea'],
#       u'api_id': u'53cc4532-8a7a-11e4-96e3-22000abcb9af'
# }
