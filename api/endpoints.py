import plivo

client = plivo.RestClient("YOUR_AUTH_ID","YOUR_AUTH_TOKEN")

# Create an Endpoint
response = client.endpoints.create(
    username="testusername",  # The username for the endpoint to be created
    password="testpassword",  # The password for your endpoint username
    alias="Test Account",  # Alias for this endpoint
)
print(response)

# Samplesuccessful output
# {
#    "username":"zumba131031145958",
#    "alias":"zumba",
#    "message":"created",
#    "endpoint_id":"37371860103666",
#    "api_id":"1c13de4c-423d-11e3-9899-22000abfa5d5"
# }


# Get details of all existing endpoints
response = client.endpoints.list(
    limit=5,  # The number of results per page
    offset=0,  # The number of value items by which the results should be offset
)
print(response)

# Sample successful output
# {
#    "api_id":"30a0c8c2-110c-11e4-bd8a-12313f016a39",
#    "meta":{
#       "limit":20,
#       "next":null,
#       "offset":0,
#       "previous":null,
#       "total_count":11
#    },
#    "objects":[
#       {
#          "alias":"callme",
#          "application":"/v1/Account/MAXXXXXXXXXXXXXXXXXX/Application/33406267401237901/",
#          "endpoint_id":"32866729519064",
#          "resource_uri":"/v1/Account/MAXXXXXXXXXXXXXXXXXX/Endpoint/32866729519064/",
#          "sip_contact":"sip:callme140703093224@122.172.71.207:57563;ob",
#          "sip_expires":"2014-07-21 19:26:08",
#          "sip_registered":"true",
#          "sip_uri":"sip:callme140703093944@phone.plivo.com",
#          "sip_user_agent":"Telephone 1.1.4",
#          "sub_account":null,
#          "username":"callme140703093944"
#       },
#       {
#          "alias":"polycom",
#          "application":"/v1/Account/MAXXXXXXXXXXXXXXXXXX/Application/37961981447734951/",
#          "endpoint_id":"17551316589618",
#          "resource_uri":"/v1/Account/MAXXXXXXXXXXXXXXXXXX/Endpoint/17551316589618/",
#          "sip_registered":"false",
#          "sip_uri":"sip:polycom140506175228@phone.plivo.com",
#          "sub_account":null,
#          "username":"polycom140506175448"
#       }
#    ]
# }

# Print the total number of apps
print (response['meta']['total_count'])

# Sample successful output
# 11

# Get details of a single endpoint
response = client.endpoints.get(
    endpoint_id="39452475478853",  # ID of the endpoint for which the details have to be retrieved
)
print(response)

# Sample successful output
# {
#    "alias":"zumba",
#    "api_id":"39015de8-4fb3-11e4-a2d1-22000ac5040c",
#    "application":"/v1/Account/MAXXXXXXXXXXXXXXXXXX/Application/379619814477342321/",
#    "endpoint_id":"39452475478853",
#    "password":"8bc0002a467b8276aaaf47e92bc46b9f",
#    "resource_uri":"/v1/Account/MAXXXXXXXXXXXXXXXXXX/Endpoint/39452475478853/",
#    "sip_registered":"false",
#    "sip_uri":"sip:zumba141009125224@phone.plivo.com",
#    "sub_account":null,
#    "username":"zumba141009125224"
# }

# Modify an endpoint
response = client.endpoints.update(
    endpoint_id="21784177241578", # ID of the endpoint that has to be modified
    alias="Double time.", # Values that have to be updated
)
print(response)

# Sample successful output
# {
#     "api_id": "a0dd783d-509c-11eb-b4f1-0242ac110003",
#     "message": "changed"
# }

# Delete an endpoint
response = client.endpoints.delete(
    endpoint_id="14659095951490", # ID of the endpoint that as to be deleted
)
print(response)

# Sample successful endpoint
# (204, '')

# Sample unsuccessful output
# {
#       'api_id': 'b6d258ee-8f64-11e4-b153-22000abcaa64', 
#	'error': 'not found'
# }
