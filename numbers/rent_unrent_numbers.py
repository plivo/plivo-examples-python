import plivo

client = plivo.RestClient("YOUR_AUTH_ID","YOUR_AUTH_TOKEN")

# Search for new number
response = client.numbers.search(
    country_iso="GB",  # The ISO code A2 of the country
    type="local",  # The type of number you are looking for. The possible number types are local, national and tollfree.
    pattern="210",  # Represents the pattern of the number to be searched.
    region="Texas",  # This filter is only applicable when the number_type is local. Region based filtering can be performed.
)
print(response)

# Sample successful output
# {
#    "api_id":"859428b0-1c88-11e4-a2d1-22000ac5040c",
#    "meta":{
#       "limit":20,
#       "next":null,
#       "offset":0,
#       "previous":null,
#       "total_count":9
#    },
#    "objects":[
#       {
#          "number":"14154009186",
#          "prefix":"415",
#          "city":"NEW YORK",
#          "country":"UNITED STATES",
#          "region":"United States",
#          "rate_center":"SNFC CNTRL",
#          "lata":722,
#          "type":"fixed",
#          "sub_type":"local",
#          "setup_rate":"0.00000",
#          "monthly_rental_rate":"0.80000",
#          "sms_enabled":true,
#          "sms_rate":"0.00800",
#          "voice_enabled":true,
#          "voice_rate":"0.00500",
#          "restriction":null,
#          "restriction_text":null,
#          "resource_uri":"/v1/Account/MAXXXXXXXXXXXXXXXXXX/PhoneNumber/14154009186/"
#       },
#       {
#          "number":"14154009187",
#          "prefix":"415",
#          "city":"NEW YORK",
#          "country":"UNITED STATES",
#          "region":"United States",
#          "rate_center":"SNFC CNTRL",
#          "lata":722,
#          "type":"fixed",
#          "sub_type":"local",
#          "setup_rate":"0.00000",
#          "monthly_rental_rate":"0.80000",
#          "sms_enabled":true,
#          "sms_rate":"0.00800",
#          "voice_enabled":true,
#          "voice_rate":"0.00500",
#          "restriction":null,
#          "restriction_text":null,
#          "resource_uri":"/v1/Account/MAXXXXXXXXXXXXXXXXXX/PhoneNumber/14154009187/"
#       }
#    ]
# }

# Buy a phone number
response = client.numbers.buy(
        number='12109206499' # The phone number
        )
print(response)

# Sample Output
# {
#    "api_id":"aa52882c-1c88-11e4-bd8a-12313f016a39",
#    "message":"created",
#    "numbers":[
#       {
#          "number":"12143010249",
#          "status":"Success"
#       }
#    ],
#    "status":"fulfilled"
# }

# For Countries Which Verification Requirements, 
# An Email Is Sent To The Registered Email With The Requirements And You Will Receive The Below Response.

# {
#    "api_id":"aa52882c-1c88-11e4-bd8a-12313f016a39",
#    "message":"created",
#    "numbers":[
#       {
#          "number":"12143010249",
#          "status":"pending"
#       }
#    ],
#    "status":"fulfilled"
# }

# Modify alias of a number
response = client.numbers.update(
    number="12143010249",  # Number that has to be modified
    alias="Updated Alias",  # The textual name given to the number
)
print(response)

# Sample successful output
# {
#   "message": "changed",
#   "api_id": "5a9fcb68-582d-11e1-86da-6ff39efcb949"
# }

# Modify the application linked to a number
response = client.numbers.update(
    number="12143010249",  # Number that has to be modified
    app_id="16638156474000802",  # The application id of the application that is to be linked
)
print(response)

# Sample successful output
# {
#   "message": "changed",
#   "api_id": "5a9fcb68-582d-11e1-86da-6ff39efcb949"
# }

# Unrent a number
response = client.numbers.delete(
    number="12143010249",  # Number that has to be unrented
)
print(response)

# Sample successful output
# (204, '')

# Sample unsuccessful output
#{
#  'api_id': '7c33ff78-8f53-11e4-b932-22000ac50fac', 
#  'error': u'not found'
#}
