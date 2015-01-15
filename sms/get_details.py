import plivo

auth_id = "Your AUTH_ID"
auth_token = "Your Auth_TOKEN"

p = plivo.RestAPI(auth_id, auth_token)

params = {
        'message_uuid': '0936ec98-7c4c-11e4-9bd8-22000afa12b9' # Message UUID for which the details have to be retrieved
}

response = p.get_message(params)

 # Prints the number of SMS units
print "Your SMS was split into %s units" % response[1]['units']

# Sample successful output
# Your SMS was split into 4 units

# Prints the status of the message
print response[1]['message_state']

# Sample successful output
# delivered

# Prints all the details of a message
print str(response)

# Sample successful output
# (200, {
#               u'message_state': u'delivered',
#               u'total_amount': u'0.02600',
#               u'to_number': u'3333333333',
#               u'total_rate': u'0.00650',
#               u'api_id': u'ebe64d72-8a75-11e4-ac1f-22000ac51de6',
#               u'message_direction': u'outbound',
#               u'from_number': u'1111111111',
#               u'message_uuid': u'0936ec98-7c4c-11e4-9bd8-22000afa12b9',
#               u'message_time': u'2014-12-05 12:27:54+05:30',
#               u'units': 4,
#               u'message_type': u'sms',
#               u'resource_uri': u'/v1/Account/XXXXXXXXXXXX/Message/0936ec98-7c4c-11e4-9bd8-22000afa12b9/'
#       }
# )
