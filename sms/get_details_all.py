import plivo

auth_id = "Your AUTH_ID"
auth_token = "Your AUTH_TOKEN"

p = plivo.RestAPI(auth_id, auth_token)

response = p.get_messages()


# Prints the complete response
print str(response)

# Sample successful output
# (200, {
#	u'meta': {
#		u'previous': None, 
#		u'total_count': 247, 
#		u'offset': 0, 
#		u'limit': 3, 
#		u'next': u'/v1/Account/XXXXXXXXXXXXXXX/Message/?limit=3&offset=3'
#	}, 
#	u'objects': [
#		{
#			u'message_state': u'sent', 
#			u'total_amount': u'0.00650', 
#			u'to_number': u'14155069431', 
#			u'total_rate': u'0.00650', 
#			u'message_direction': u'outbound', 
#			u'from_number': u'18583650866', 
#			u'message_uuid': u'1aead330-8ff9-11e4-9bd8-22000afa12b9', 
#			u'message_time': u'2014-12-30 11:54:38+04:00', 
#			u'units': 1, 
#			u'message_type': u'sms', 
#			u'resource_uri': u'/v1/Account/XXXXXXXXXXXXXXX/Message/1aead330-8ff9-11e4-9bd8-22000afa12b9/'
#		}, 
#		{
#			u'message_state': u'delivered', 
#			u'total_amount': u'0.00000', 
#			u'to_number': u'18583650866', 
#			u'total_rate': u'0.00000', 
#			u'message_direction': u'inbound', 
#			u'from_number': u'14155069431', 
#			u'message_uuid': u'15fbd64e-8ff9-11e4-b1a4-22000ac693b1', 
#			u'message_time': u'2014-12-30 11:54:30+04:00', 
#			u'units': 1, 
#			u'message_type': u'sms', 
#			u'resource_uri': u'/v1/Account/XXXXXXXXXXXXXXX/Message/15fbd64e-8ff9-11e4-b1a4-22000ac693b1/'
#		}, 
#		{
#			u'message_state': u'sent', 
#			u'total_amount': u'0.01300', 
#			u'to_number': u'14155069431', 
#			u'total_rate': u'0.00650', 
#			u'message_direction': u'outbound', 
#			u'from_number': u'18583650866', 
#			u'message_uuid': u'745b7cca-8f9b-11e4-a77d-22000ae383ea', 
#			u'message_time': u'2014-12-30 00:44:16+04:00', 
#			u'units': 2, 
#			u'message_type': u'sms', 
#			u'resource_uri': u'/v1/Account/XXXXXXXXXXXXXXX/Message/745b7cca-8f9b-11e4-a77d-22000ae383ea/'
#		}
#	], 
#		u'api_id': u'625944ba-9259-11e4-96e3-22000abcb9af'
#	}
# )

# Prints the details of sent messages
print response[1]['objects']

# Sample successful output
#[
#       {
#               u'message_state': u'delivered',
#               u'total_amount': u'0.00650',
#               u'to_number': u'2222222222',
#               u'total_rate': u'0.00650',
#               u'message_direction': u'outbound',
#               u'from_number': u'1111111111',
#               u'message_uuid': u'2d55d550-8a73-11e4-9bd8-22000afa12b9',
#               u'message_time': u'2014-12-23 12:43:21+05:30',
#               u'units': 1,
#               u'message_type': u'sms',
#               u'resource_uri': u'/v1/Account/XXXXXXXXXXXXXXX/Message/2d55d550-8a73-11e4-9bd8-22000afa12b9/'
#       },
#       {
#               u'message_state': u'delivered',
#               u'total_amount': u'0.00650',
#               u'to_number': u'2222222222',
#               u'total_rate': u'0.00650',
#               u'message_direction': u'outbound',
#               u'from_number': u'1111111111',
#               u'message_uuid': u'2d5617e0-8a73-11e4-89de-22000ae885b8',
#               u'message_time': u'2014-12-23 12:43:21+05:30',
#               u'units': 1,
#               u'message_type': u'sms',
#               u'resource_uri': u'/v1/Account/XXXXXXXXXXXXXXX/Message/2d5617e0-8a73-11e4-89de-22000ae885b8/'
#       }
# ]

# Filtering the records

params = {
    'limit': '10', # The number of results per page
    'offset' : '0', # The number of value items by which the results should be offset
    'message_state' : "delivered", # The state of the message to be filtered
    'message_direction' : "inbound", # The direction of te message to be fltered
    'subaccount' : "SubAccount_AUTH_ID" # The id of the subaccount, if SMS details of the subaccount is needed.
    }

response = p.get_messages(params)
print str(response)

# Sample successful output
# (200, {
#       u'meta': {
#               u'previous': None,
#               u'total_count': 215,
#               u'offset': 0,
#               u'limit': 10,
#               u'next': u'/v1/Account/XXXXXXXXXXXXXXX/Message/?limit=10&offset=10'
#       },
#       u'objects': [
#               {
#                       u'message_state': u'delivered',
#                       u'total_amount': u'0.00650',
#                       u'to_number': u'2222222222',
#                       u'total_rate': u'0.00650',
#                       u'message_direction': u'inbound',
#                       u'from_number': u'1111111111',
#                       u'message_uuid': u'2d55d550-8a73-11e4-9bd8-22000afa12b9',
#                       u'message_time': u'2014-12-23 12:43:21+05:30',
#                       u'units': 1,
#                       u'message_type': u'sms',
#                       u'resource_uri': u'/v1/Account/XXXXXXXXXXXXXXX/Message/2d55d550-8a73-11e4-9bd8-22000afa12b9/'
#               },
#               {
#                       u'message_state': u'delivered',
#                       u'total_amount': u'0.00650',
#                       u'to_number': u'2222222222',
#                       u'total_rate': u'0.00650',
#                       u'message_direction': u'inbound',
#                       u'from_number': u'1111111111',
#                       u'message_uuid': u'2d5617e0-8a73-11e4-89de-22000ae885b8',
#                       u'message_time': u'2014-12-23 12:43:21+05:30',
#                       u'units': 1,
#                       u'message_type': u'sms',
#                       u'resource_uri': u'/v1/Account/XXXXXXXXXXXXXXX/Message/2d5617e0-8a73-11e4-89de-22000ae885b8/'
#               }
#       ]
# )

# Prints only the From-Number, To-Number and Message-State
for message in response[1]['objects']:
    print message['from_number'], message['to_number'],message['message_state']

# Sample successful output
# 1111111111 3333333333 delivered
# 1111111111 3333333333 delivered
# 2222222222 1111111111 delivered
# 2222222222 1111111111 delivered
# 2222222222 1111111111 delivered
# 2222222222 1111111111 delivered
# 1111111111 3333333333 delivered
# 1111111111 3333333333 delivered
# 1111111111 3333333333 delivered
# 1111111111 3333333333 delivered


