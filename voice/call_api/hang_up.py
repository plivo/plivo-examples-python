import plivo

client = plivo.RestClient("YOUR_AUTH_ID", "YOUR_AUTH_TOKEN")

response = client.calls.delete(
    call_uuid="3a2e4c90-dcee-4931-8a59-f123ab507e60",  # UUID of the call to be hung up
)
print(response)


# Sample successful output
# (204,'')

# Sample unsuccesful output
# {
#   'api_id': '790ca696-9012-11e4-b932-22000ac50fac', 
#	'error': 'call not found'
#}