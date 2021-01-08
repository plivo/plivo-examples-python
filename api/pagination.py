import plivo

client = plivo.RestClient("YOUR_AUTH_ID","YOUR_AUTH_TOKEN")

# This example shows how to traverse the list of all applications. 

# Get details all existing applications
response = client.applications.list(
    offset=0, # The number of results per page
    limit=5, # The number of value items by which the results should be offset
)
print(response)

# Sample successful output
# {
#    {
#       "limit":5,
#       "next":"/v1/Account/MAXXXXXXXXXXXXXXXXXX/Application/?limit=5&offset=5",
#       "offset":0,
#       "previous":"None",
#       "total_count":4
#    }
#    "objects": [{
#    "answer_method":"GET",
#    "answer_url":"http://plivodirectdial.herokuapp.com/",
#    "app_id":"77506472664956327",
#    "app_name":"Direct Dial",
#    "application_type":"XML",
#    "default_app":false,
#    "default_endpoint_app":true,
#    "enabled":true,
#    "fallback_answer_url":"",
#    "fallback_method":"POST",
#    "hangup_method":"POST",
#    "hangup_url":"http://plivodirectdial.herokuapp.com/",
#    "log_incoming_message":true,
#    "message_method":"POST",
#    "message_url":"http://plivodirectdial.herokuapp.com/",
#    "public_uri":false,
#    "resource_uri":"/v1/Account/MAXXXXXXXXXXXXXXXXXX/Application/77506472664956327/",
#    "sip_uri":"sip:20372631212782780@app.plivo.com",
#    "sub_account":"None"
# },
# {
#    "answer_method":"POST",
#    "answer_url":"http://plivodirectdial.herokuapp.com/",
#    "app_id":"11624750585743683",
#    "app_name":"app name",
#    "application_type":"XML",
#    "default_app":false,
#    "default_endpoint_app":false,
#    "enabled":true,
#    "fallback_answer_url":"None",
#    "fallback_method":"POST",
#    "hangup_method":"POST",
#    "hangup_url":"http://plivodirectdial.herokuapp.com/",
#    "log_incoming_message":true,
#    "message_method":"POST",
#    "message_url":"None",
#    "public_uri":false,
#    "resource_uri":"/v1/Account/MAXXXXXXXXXXXXXXXXXX/Application/11624750585743683/",
#    "sip_uri":"sip:20372631212782780@app.plivo.com",
#    "sub_account":"None"
# },
# {
#    "answer_method":"POST",
#    "answer_url":"http://plivodirectdial.herokuapp.com/",
#    "app_id":"17371468466407823",
#    "app_name":"Trainig",
#    "application_type":"XML",
#    "default_app":false,
#    "default_endpoint_app":false,
#    "enabled":true,
#    "fallback_answer_url":"",
#    "fallback_method":"POST",
#    "hangup_method":"POST",
#    "hangup_url":"http://plivodirectdial.herokuapp.com/",
#    "log_incoming_message":true,
#    "message_method":"POST",
#    "message_url":"",
#    "public_uri":false,
#    "resource_uri":"/v1/Account/MAXXXXXXXXXXXXXXXXXX/Application/17371468466407823/",
#    "sip_uri":"sip:20372631212782780@app.plivo.com",
#    "sub_account":"None"
# },
# {
#    "answer_method":"POST",
#    "answer_url":"http://plivodirectdial.herokuapp.com/",
#    "app_id":"28596691685931059",
#    "app_name":"AppTest-1558568",
#    "application_type":"XML",
#    "default_app":false,
#    "default_endpoint_app":false,
#    "enabled":true,
#    "fallback_answer_url":"",
#    "fallback_method":"POST",
#    "hangup_method":"POST",
#    "hangup_url":"http://plivodirectdial.herokuapp.com/",
#    "log_incoming_message":true,
#    "message_method":"POST",
#    "message_url":"",
#    "public_uri":false,
#    "resource_uri":"/v1/Account/MAXXXXXXXXXXXXXXXXXX/Application/28596691685931059/",
#    "sip_uri":"sip:20372631212782780@app.plivo.com",
#    "sub_account":"None"
# }]
# }

# Print the link to view the next page of results
print (response['meta']['next'])

# Sample successful output
# /v1/Account/XXXXXXXXXXXX/Application/?limit=2&offset=2
# Browse https://api.plivo.com/v1/Account/XXXXXXXXXXXX/Application/?limit=2&offset=2
# to view the next page of results. To traverse pages, browse the 'next' and 'previous' urls