import plivo

client = plivo.RestClient("YOUR_AUTH_ID","YOUR_AUTH_TOKEN")

# Create a new application
response = client.applications.create(
    app_name="Test Application",  # The name of your application
    answer_url="http://answer.url",  # The URL Plivo will fetch when a call executes this application
)
print(response)

# Sample successful output
# {
#   "message": "created",
#   "app_id": "15784735442685051",
#   "api_id": "5a9fcb68-582d-11e1-86da-6ff39efcb949"
# }

# Get details all existing applications

response = client.applications.list(
    offset=0,  # The number of value items by which the results should be offset
    limit=5,  # The number of results per page
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

# Print the total number of apps
print(response['meta']['total_count'])

# Sample successful output
# 4

# Get details of a single application
response = client.applications.get(
    app_id="24075895272788587",  # ID of the application for which the details have to be retrieved
)
print(response)

# Sample successful output
# {
#    "answer_method":"POST",
#    "answer_url":"http://plivodirectdial.herokuapp.com/",
#    "app_id":"28596691685931059",
#    "api_id": "874df593-5049-11eb-8445-0242ac110003",
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
# }

# Modify an application
response = client.applications.update(
    app_id="21686794894743506",  # ID of the application that has to be modified
    answer_url="http://updated.answer.url",  # Values that have to be updated
)
print(response)

# Sample successful output
# {
#    "message":"changed",
#    "api_id":"5a9fcb68-582d-11e1-86da-6ff39efcb949"
# }

# Delete an application
response = client.applications.delete(
    app_id = "21686794894743506", #ID of the application that as to be deleted
)
print(response)

# Sample successful output
# (204, '')

# Sample unsuccessful output
# {
#    'api_id': u'5fbdd916-8f64-11e4-b153-22000abcaa64', 
#    'error': u'not found'
# }