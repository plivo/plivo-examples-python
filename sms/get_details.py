import plivo

client = plivo.RestClient("YOUR_AUTH_ID", "YOUR_AUTH_TOKEN")

response = client.messages.get(
        message_uuid='f597df14-50af-11eb-b38e-0242ac110004',# Message UUID for which the details have to be retrieved
)
 # Prints the number of SMS units
print ("Your SMS was split into %s units" % response['units'])

# Sample successful output
# Your SMS was split into 4 units

# Prints the status of the message
print (response['message_state'])

# Sample successful output
# delivered

# Prints all the details of a message
print(response)

# Sample successful output
# {
#    "error_code":"200",
#    "from_number":"18552828641",
#    "message_direction":"inbound",
#    "message_state":"delivered",
#    "message_time":"2016-08-17 21:22:36+05:30",
#    "message_type":"sms",
#    "message_uuid":"2a340179-e8a9-4b1d-ae2c-9f346e7b6d7d",
#    "resource_uri":"/v1/Account/{auth_id}/Message/2a340179-e8a9-4b1d-ae2c-9f346e7b6d7d/",
#    "to_number":"19352326448",
#    "total_amount":"0.00000",
#    "total_rate":"0.00350",
#    "units":1
# }