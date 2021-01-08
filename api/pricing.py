import plivo

client = plivo.RestClient("YOUR_AUTH_ID","YOUR_AUTH_TOKEN")

response = client.pricing.get(
    country_iso="GB",  # The 2 digit country ISO code.
)
print(response)

# Sample successful output
# {
#    "api_id":"7ff5505c-93ca-11e7-9bde-024427e23b8a",
#    "country":"United States",
#    "country_code":1,
#    "country_iso":"US",
#    "message":{
#       "inbound":{
#          "rate":"0.00000"
#       },
#       "outbound":{
#          "rate":"0.00350"
#       },
#       "outbound_networks_list":[
#          {
#             "group_name":"US",
#             "rate":"0.00350"
#          },
#          {
#             "group_name":"United States - AT&T Mobility",
#             "rate":"0.00350"
#          }
#       ]
#    },
#    "phone_numbers":{
#       "local":{
#          "rate":"0.80000"
#       },
#       "tollfree":{
#          "rate":"1.00000"
#       }
#    },
#    "voice":{
#       "inbound":{
#          "ip":{
#             "rate":"0.00300"
#          },
#          "local":{
#             "rate":"0.00850"
#          },
#          "tollfree":{
#             "rate":"0.02100"
#          }
#       },
#       "outbound":{
#          "ip":{
#             "rate":"0.00300"
#          },
#          "local":{
#             "rate":"0.00750"
#          },
#          "rates":[
#             {
#                "prefix":[
#                   "1"
#                ],
#                "rate":"0.00750"
#             }
#          ],
#          "tollfree":{
#             "rate":null
#          }
#       }
#    }
# }