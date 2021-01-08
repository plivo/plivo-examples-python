import plivo

client = plivo.RestClient("YOUR_AUTH_ID", "YOUR_AUTH_TOKEN")
response = client.live_calls.list_ids()
print(response)


# Sample successful output
# {
#    "api_id":"c9527676-5839-11e1-86da-6ff39efcb949",
#    "calls":[
#       "eac94337-b1cd-499b-82d1-b39bca50dc31",
#       "0a70a7fb-168e-4944-a846-4f3f4d2f96f1"
#    ]
# }

# Looping through the call uuids
for uuid in response['calls']:
    print (uuid)

# Sample successful output
# eac94337-b1cd-499b-82d1-b39bca50dc31
# 0a70a7fb-168e-4944-a846-4f3f4d2f96f1
