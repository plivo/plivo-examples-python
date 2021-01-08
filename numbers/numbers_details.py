import plivo

client = plivo.RestClient("YOUR_AUTH_ID","YOUR_AUTH_TOKEN")

# Get all numbers

response = client.numbers.list(
    limit=5,
    offset=0,
)
print(response)

# Sample successful output
# {
#    "api_id":"114de006-1c95-11e4-8a4a-123140008edf",
#    "meta":{
#       "limit":3,
#       "next":"/v1/Account/MAXXXXXXXXXXXXXXXXXX/Number/?limit=3&offset=3",
#       "offset":0,
#       "previous":null,
#       "total_count":20
#    },
#    "objects":[
#       {
#          "number":"18135401302",
#          "alias":null,
#          "sub_account":null,
#          "added_on":"2014-08-05",
#          "application":"/v1/Account/MAXXXXXXXXXXXXXXXXXX/Application/29986316244302815/",
#          "carrier":"Plivo",
#          "region":"Florida, UNITED STATES",
#          "number_type":"local",
#          "monthly_rental_rate":"0.80000",
#          "sms_enabled":true,
#          "sms_rate":"0.00000",
#          "voice_enabled":true,
#          "voice_rate":"0.00850",
#          "resource_uri":"/v1/Account/MAXXXXXXXXXXXXXXXXXX/Number/18135401302/"
#       },
#       {
#          "number":"14153661106",
#          "alias":"",
#          "sub_account":null,
#          "added_on":"2013-01-01",
#          "application":"/v1/Account/MAXXXXXXXXXXXXXXXXXX/Application/16632559604105954/",
#          "carrier":"Plivo",
#          "region":"BELVEDERE, UNITED STATES",
#          "number_type":"local",
#          "monthly_rental_rate":"0.80000",
#          "sms_enabled":true,
#          "sms_rate":"0.00000",
#          "voice_enabled":true,
#          "voice_rate":"0.00850",
#          "resource_uri":"/v1/Account/MAXXXXXXXXXXXXXXXXXX/Number/14153661106/"
#       }
#    ]
# }

# Get a particular number
response = client.numbers.get(
    number="133084444444",  # PHone number for which the details have to be retrieved
)
print(response)

# Sample successful output
# {
#     "active": true,
#     "added_on": "2020-12-24",
#     "alias": "",
#     "api_id": "540544bc-50a4-11eb-8067-0242ac110005",
#     "application": null,
#     "carrier": "Plivo",
#     "city": "Lisbon",
#     "compliance_application_id": null,
#     "compliance_status": null,
#     "country": "United States",
#     "mms_enabled": true,
#     "mms_rate": "0.00400",
#     "monthly_rental_rate": "0.18000",
#     "number": "133084444444",
#     "number_type": "local",
#     "region": "Ohio, UNITED STATES",
#     "resource_uri": "/v1/Account/MAXXXXXXXXXXX/Number/133084444444/",
#     "sms_enabled": true,
#     "sms_rate": "0.00000",
#     "sub_account": null,
#     "type": "local",
#     "verification_info": [],
#     "voice_enabled": true,
#     "voice_rate": "0.00300"
# }

