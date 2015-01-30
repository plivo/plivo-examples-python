import plivo

auth_id = "Your AUTH_ID"
auth_token = "Your Auth_TOKEN"

p = plivo.RestAPI(auth_id, auth_token)

params = {
    'src': '1111111111', # Sender's phone number with country code
    'dst' : '2222222222<3333333333', # Receivers' phone numbers with country code. The numbers are separated by "<" delimiter.
    'text' : "Hi, from Plivo" # Your SMS Text Message
}

response = p.send_message(params)

# Print the entire response
print str(response)

# Sample sucessful output
# (202, {
#       u'message': u'message(s) queued',
#       u'message_uuid': [
#               u'2d55d550-8a73-11e4-9bd8-22000afa12b9',
#               u'2d5617e0-8a73-11e4-89de-22000ae885b8'
#       ],
#       u'api_id': u'2d30af46-8a73-11e4-96e3-22000abcb9af'
#       }
# )

# Print only the status code
print response[0]

# Sample successful output
# 202

# Print the message uuid
print response[1]['message_uuid']

# Sample successful output
#[
#       u'2d55d550-8a73-11e4-9bd8-22000afa12b9',
#       u'2d5617e0-8a73-11e4-89de-22000ae885b8'
#]

# Loop through the message uuids

for uuid in response[1]['message_uuid']:
    print uuid

# Sample successful output
#       2d55d550-8a73-11e4-9bd8-22000afa12b9
#       2d5617e0-8a73-11e4-89de-22000ae885b8

# When an invalid number is given as dst parameter, an error will be thrown and the message will not be sent

params = {
    'src': '1111111111', # Sender's phone number with country code
    'dst' : '2222222222<333333', # Receivers' phone numbers with country code. The numbers are separated by "<" delimiter.
    'text' : "Hi, from Plivo" # Your SMS Text Message
}

response = p.send_message(params)

# Print the entire response
print str(response)

# Sample output
# (400, {
#   u'api_id': u'6b07a5de-8f7f-11e4-b932-22000ac50fac', 
#   u'error': u'1111111 is not a valid phone number'
#   }
# )
