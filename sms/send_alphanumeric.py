import plivo

client = plivo.RestClient("auth_id", "auth_token")
response = client.messages.create(
    src="TEST",  # Alphanumeric sender ID
    dst=" 14152223333",  # Sender's phone number with country code
    text="Hello, this is a sample text",  # Your SMS Text Message - English
    url="http://foo.com/sms_status/",  # URL for callback
    method="GET",  # The method used to call the url
)
# Prints the complete response
print(response)

# Sample successful output
# {
#    "message":"message(s) queued",
#    "message_uuid":[
#       "db3ce55a-7f1d-11e1-8ea7-1231380bc196"
#    ],
#    "api_id":"db342550-7f1d-11e1-8ea7-1231380bc196"
# }