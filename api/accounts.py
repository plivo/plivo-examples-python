import plivo

client = plivo.RestClient("YOUR_AUTH_ID","YOUR_AUTH_TOKEN")

# Get account details
response = client.account.get()
print(response)

# Sample successful output
# {
#    "account_type":"standard",
#    "address":"Wayne Enterprises Inc.",
#    "api_id":"150892a0-922a-11e7-b6f4-061564b78b75",
#    "auth_id":"MAXXXXXXXXXXXXXXXXXX",
#    "auto_recharge":false,
#    "billing_mode":"prepaid",
#    "cash_credits":"1.80900",
#    "city":"Gotham",
#    "name":"Bruce Wayne",
#    "resource_uri":"/v1/Account/MAXXXXXXXXXXXXXXXXXX/",
#    "state":"NY",
#    "timezone":"America/New_York"
# }

# Modify account
response = client.account.update(
    name="Lucius Fox",  # Name of the account holder or business.
    city="New York",  # City of the account holder
    address="Times Square",  # Address of the account holder
)
print(response)


# Sample successful output
# {
#   "api_id": "02bbdbaa-9303-11e7-8bc8-065f6a74a84a",
#   "message": "changed"
# }

# Create a sub account
response = client.subaccounts.create(
    name="Wayne Enterprises Subaccount",  # Name of the subaccount
    enabled=True,  # Specify if the subaccount should be enabled or not
)
print(response)

# Sample successful output
# {
# 	"api_id": "324a7dd8-0db2-11e4-8a4a-123140008edf",
# 	"auth_id": "SAXXXXXXXXXXXXXXXXXX",
# 	"auth_token": "MTZjYWM0YzVjNjMwZmVmODFiNWJjNPJmOGJjZjgw",
# 	"message": "created"
# }

# Modify a sub account
response = client.subaccounts.update(
    auth_id="SAXXXXXXXXXXXXXXXXXX",
    name="Updated Subaccount Name",
)
print(response)

# Sample successful output
# {
#   "message": "changed",
#   "api_id": "5a9fcb68-523d-11e1-86da-6ff39efcb949"
# }

# Get details of all sub accounts
response = client.subaccounts.list(
    offset=0, # The number of value items by which the results should be offset
    limit=5, # The number of results per page
)
print(response)

# Sample successful output
# {
#    "api_id":"b38bf42e-0db4-11e4-8a4a-123140008edf",
#    "meta":{
#       "limit":20,
#       "next":null,
#       "offset":0,
#       "previous":null,
#       "total_count":2
#    },
#    "objects":[
#       {
#          "account":"/v1/Account/MAXXXXXXXXXXXXXXXXXX/",
#          "auth_id":"SAXXXXXXXXXXXXXXXXXX",
#          "auth_token":"MTZjYWM0YzVjNjMwZmVmODFiNWJjNWJmOGJjZjgw",
#          "created":"2014-07-17",
#          "enabled":false,
#          "modified":null,
#          "name":"Chewbacca",
#          "resource_uri":"/v1/Account/MAXXXXXXXXXXXXXXXXXX/Subaccount/SAXXXXXXXXXXXXXXXXXX/"
#       },
#       {
#          "account":"/v1/Account/MAXXXXXXXXXXXXXXXXXX/",
#          "auth_id":"SAXXXXXXXXXXXXXXXXXX",
#          "auth_token":"OTdhMjYwMWYxOGMyNpFjNzUwYWM3YWI3NjY4Y2Ey",
#          "created":"2012-09-23",
#          "enabled":true,
#          "modified":"2012-09-23",
#          "name":"new",
#          "resource_uri":"/v1/Account/MAXXXXXXXXXXXXXXXXXX/Subaccount/SAXXXXXXXXXXXXXXXXXX/"
#       }
#    ]
# }

# Print the total number of apps
print (response['meta']['total_count'])

# Sample successful output
# 2

# Get details of a particular sub acount

response = client.subaccounts.get(
    auth_id='SAXXXXXXXXXXXXXXXXXX', # Auth ID of the sub acccount for which the details hae to be retrieved
    )
print(response)

# Sample successful output
# {
#    "account":"/v1/Account/MAXXXXXXXXXXXXXXXXXX/",
#    "api_id":"323972b2-0db3-11e4-a2d1-22000ac5040c",
#    "auth_id":"SAXXXXXXXXXXXXXXXXXX",
#    "auth_token":"MTZjYWM0YzVjNjMwZmVmODFiNWJjNWJmOGJjZjgw",
#    "created":"2014-07-17",
#    "enabled":false,
#    "modified":null,
#    "name":"Han Solo",
#    "resource_uri":"/v1/Account/MAXXXXXXXXXXXXXXXXXX/Subaccount/SAXXXXXXXXXXXXXXXXXX/"
# }

# Delete a sub account
response = client.subaccounts.delete(
    auth_id="SAXXXXXXXXXXXXXXXXXX",  # Auth ID of the sub acccount that has to be deleted
    cascade=True,  # If cascade is set to true, the Applications, Endpoints, and Numbers associated with the Subaccount are also deleted
)
print(response)

# Sample successful output
# (204, '')

# Sample unsuccessful output
# {
#    'api_id': '28eb91a2-8f65-11e4-a2d1-22000ac5040c', 
#    'error': 'not found'
# }
