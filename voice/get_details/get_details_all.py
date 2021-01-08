import plivo

client = plivo.RestClient("YOUR_AUTH_ID", "YOUR_AUTH_TOKEN")

response = client.calls.list(
    limit=5,
    offset=0,
)
print(response)

# {
#    "api_id":"8299d094-dc72-11e5-b56c-22000ae90795",
#    "meta":{
#       "limit":20,
#       "next":null,
#       "offset":0,
#       "previous":null,
#       "total_count":4
#    },
#    "objects":[
#       {
#          "answer_time":"2015-07-26 15:45:02+05:30",
#          "api_id":"06ae0f8f-dc72-11e5-b56c-22000ae90795",
#          "bill_duration":924,
#          "billed_duration":960,
#          "call_direction":"outbound",
#          "call_duration":924,
#          "call_uuid":"eba53b9e-8fbd-45c1-9444-696d2172fbc8",
#          "end_time":"2015-07-26 15:45:14+05:30",
#          "from_number":"+14158572518",
#          "initiation_time":"2015-07-26 15:44:49+05:30",
#          "parent_call_uuid":null,
#          "resource_uri":"/v1/Account/MAXXXXXXXXXXXXXXXXXX/Call/eba53b9e-8fbd-45c1-9444-696d2172fbc8/",
#          "to_number":"14153268174",
#          "total_amount":"0.13600",
#          "total_rate":"0.00850"
#       },
#       {
#          "answer_time":"2015-07-26 16:45:02+05:30",
#          "api_id":"06ae0f8f-dc72-11e5-b56c-22000ae90795",
#          "bill_duration":924,
#          "billed_duration":960,
#          "call_direction":"outbound",
#          "call_duration":924,
#          "call_uuid":"eba53b9e-8fbd-45c1-9444-696d2172fbc8",
#          "end_time":"2015-07-26 16:45:14+05:30",
#          "from_number":"+14158572518",
#          "initiation_time":"2015-07-26 16:44:49+05:30",
#          "parent_call_uuid":null,
#          "resource_uri":"/v1/Account/MAXXXXXXXXXXXXXXXXXX/Call/eba53b9e-8fbd-45c1-9444-696d2172fbc8/",
#          "to_number":"14153268174",
#          "total_amount":"0.13600",
#          "total_rate":"0.00850"
#       }
#    ]
# }

# Filtering the records

response = client.calls.list(
    limit=5, # The number of results per page
    offset=0, # The number of value items by which the results should be offset
    from_number="1111111111", # Filter the results by the number from where the call originated
    to_number="2222222222", # Filter the results by the number to which the call was made
    call_direction="inbound", # Filter the results by call direction. The valid inputs are inbound and outbound
)
print(response)

# Sample successful output
# {
#    "meta":{
#       "previous":"None",
#       "total_count":2,
#       "offset":0,
#       "limit":10,
#       "next":"None"
#    },
#    "objects":[
#       {
#          "bill_duration":18,
#          "billed_duration":60,
#          "total_amount":0.00850,
#          "parent_call_uuid":"None",
#          "call_direction":"inbound",
#          "call_duration":18,
#          "to_number":2222222222,
#          "total_rate":0.00850,
#          "from_number":1111111111,
#          "end_time":"2014-12-30 16":"00":"50+04":00,
#          "call_uuid":74430d86-901b-11e4-9a96-71f618784e1e,
#          "resource_uri":/v1/Account/XXXXXXXXXXXXXXX/Call/74430d86-901b-11e4-9a96-71f618784e1e/
#       },
#       {
#          "bill_duration":13,
#          "billed_duration":60,
#          "total_amount":0.00850,
#          "parent_call_uuid":"None",
#          "call_direction":"inbound",
#          "call_duration":13,
#          "to_number":2222222222,
#          "total_rate":0.00850,
#          "from_number":1111111111,
#          "end_time":"2014-12-30 15":"59":"16+04":00,
#          "call_uuid":3f2192a8-901b-11e4-93ac-c374cdd23d80,
#          "resource_uri":/v1/Account/XXXXXXXXXXXXXXX/Call/3f2192a8-901b-11e4-93ac-c374cdd23d80/
#       }
#    ]
# }