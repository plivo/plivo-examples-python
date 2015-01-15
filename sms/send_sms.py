# -*- coding: utf-8 -*-
import plivo

auth_id = "Your AUTH_ID"
auth_token = "Your Auth_TOKEN"

p = plivo.RestAPI(auth_id, auth_token)

params = {
    'src': '1111111111', # Sender's phone number with country code
    'dst' : '2222222222', # Receiver's phone Number with country code
    'text' : u"Hello, how are you?", # Your SMS Text Message - English
#   'text' : u"こんにちは、元気ですか？" # Your SMS Text Message - Japanese
#   'text' : u"Ce est texte généré aléatoirement" # Your SMS Text Message - French
    'url' : "http://morning-ocean-4669.herokuapp.com/report/", # The URL to which with the status of the message is sent
    'method' : 'GET' # The method used to call the url
}

response = p.send_message(params)

# Prints the complete response
print str(response)

# Sample successful output
# (202,
#       {
#               u'message': u'message(s) queued',
#               u'message_uuid': [u'b795906a-8a79-11e4-9bd8-22000afa12b9'],
#               u'api_id': u'b77af520-8a79-11e4-b153-22000abcaa64'
#       }
# )

# Prints only the status code
print response[0]

# Sample successful output
# 202

# Prints the rmessage details
print response[1]

# Sample successful output
# {
#       u'message': u'message(s) queued',
#       u'message_uuid': [u'b795906a-8a79-11e4-9bd8-22000afa12b9'],
#       u'api_id': u'b77af520-8a79-11e4-b153-22000abcaa64'
# }

# Print the message message_uuid
print response[1]['message_uuid']

# Sample successful output
# [u'b795906a-8a79-11e4-9bd8-22000afa12b9']

# Print the api_id
print response[1]['api_id']

# Sample successful output
# b77af520-8a79-11e4-b153-22000abcaa64
