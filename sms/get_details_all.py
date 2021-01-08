import plivo

client = plivo.RestClient("YOUR_AUTH_ID", "YOUR_AUTH_TOKEN")

response = client.messages.list(
    limit=5,
    offset=0,
)
print(response)


# Sample successful output
# {
#    "api_id":"88415194-6df0-11e6-b608-06a72a185e87",
#    "meta":{
#       "limit":2,
#       "next":"/v1/Account/{auth_id}/Message/?limit=20&error_code=200&offset=20",
#       "offset":0,
#       "previous":null,
#       "total_count":22
#    },
#    "objects":[
#       {
#          "error_code":"200",
#          "from_number":"18552828641",
#          "message_direction":"outbound",
#          "message_state":"failed",
#          "message_time":"2016-08-17 21:26:44+05:30",
#          "message_type":"sms",
#          "message_uuid":"85ce8068-6fab-4f0a-9dc7-d6c852cdde91",
#          "resource_uri":"/v1/Account/{auth_id}/Message/85ce8068-6fab-4f0a-9dc7-d6c852cdde91/",
#          "to_number":"19352326448",
#          "total_amount":"0.00000",
#          "total_rate":"0.00350",
#          "units":1
#       },
#       {
#          "error_code":"200",
#          "from_number":"18552828641",
#          "message_direction":"outbound",
#          "message_state":"failed",
#          "message_time":"2016-08-17 21:22:36+05:30",
#          "message_type":"sms",
#          "message_uuid":"2a340179-e8a9-4b1d-ae2c-9f346e7b6d7d",
#          "resource_uri":"/v1/Account/{auth_id}/Message/2a340179-e8a9-4b1d-ae2c-9f346e7b6d7d/",
#          "to_number":"19352326448",
#          "total_amount":"0.00000",
#          "total_rate":"0.00350",
#          "units":1
#       }
#    ]
# }

# Prints the details of sent messages with no meta information.
print (response['objects'])

# Sample successful output
# {
#    "error_code":"200",
#    "from_number":"18552828641",
#    "message_direction":"outbound",
#    "message_state":"failed",
#    "message_time":"2016-08-17 21:26:44+05:30",
#    "message_type":"sms",
#    "message_uuid":"85ce8068-6fab-4f0a-9dc7-d6c852cdde91",
#    "resource_uri":"/v1/Account/{auth_id}/Message/85ce8068-6fab-4f0a-9dc7-d6c852cdde91/",
#    "to_number":"19352326448",
#    "total_amount":"0.00000",
#    "total_rate":"0.00350",
#    "units":1
# },
# {
#    "error_code":"200",
#    "from_number":"18552828641",
#    "message_direction":"outbound",
#    "message_state":"failed",
#    "message_time":"2016-08-17 21:22:36+05:30",
#    "message_type":"sms",
#    "message_uuid":"2a340179-e8a9-4b1d-ae2c-9f346e7b6d7d",
#    "resource_uri":"/v1/Account/{auth_id}/Message/2a340179-e8a9-4b1d-ae2c-9f346e7b6d7d/",
#    "to_number":"19352326448",
#    "total_amount":"0.00000",
#    "total_rate":"0.00350",
#    "units":1
# }

# Filtering the records
response = client.messages.list(
    limit=5,  # The number of results per page
    offset=0,  # The number of value items by which the results should be offset
    message_state="delivered",  # The state of the message to be filtered
    message_direction="inbound",  # The direction of te message to be fltered
    subaccount="SubAccount_AUTH_ID",  # The id of the subaccount, if SMS details of the subaccount is needed.
)
print(response)

# Sample successful output
# {
#    "api_id":"88415194-6df0-11e6-b608-06a72a185e87",
#    "meta":{
#       "limit":2,
#       "next":"/v1/Account/{auth_id}/Message/?limit=20&error_code=200&offset=20",
#       "offset":0,
#       "previous":null,
#       "total_count":22
#    },
#    "objects":[
#       {
#          "error_code":"200",
#          "from_number":"18552828641",
#          "message_direction":"inbound",
#          "message_state":"delivered",
#          "message_time":"2016-08-17 21:26:44+05:30",
#          "message_type":"sms",
#          "message_uuid":"85ce8068-6fab-4f0a-9dc7-d6c852cdde91",
#          "resource_uri":"/v1/Account/{auth_id}/Message/85ce8068-6fab-4f0a-9dc7-d6c852cdde91/",
#          "to_number":"19352326448",
#          "total_amount":"0.00000",
#          "total_rate":"0.00350",
#          "units":1
#       },
#       {
#          "error_code":"200",
#          "from_number":"18552828641",
#          "message_direction":"inbound",
#          "message_state":"delivered",
#          "message_time":"2016-08-17 21:22:36+05:30",
#          "message_type":"sms",
#          "message_uuid":"2a340179-e8a9-4b1d-ae2c-9f346e7b6d7d",
#          "resource_uri":"/v1/Account/{auth_id}/Message/2a340179-e8a9-4b1d-ae2c-9f346e7b6d7d/",
#          "to_number":"19352326448",
#          "total_amount":"0.00000",
#          "total_rate":"0.00350",
#          "units":1
#       }
#    ]
# }

# Prints only the From-Number, To-Number and Message-State
for message in response['objects']:
    print (message['from_number'], message['to_number'],message['message_state'])

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


