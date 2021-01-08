import plivo

client = plivo.RestClient("YOUR_AUTH_ID", "YOUR_AUTH_TOKEN")
response = client.messages.create(
    src="14152224444",  # Sender's phone number with country code
    dst=" 14152223333",  # Sender's phone number with country code
    text="Hello, this is a sample text",  # Your SMS Text Message - English
    #   'text' : u"こんにちは、元気ですか？" # Your SMS Text Message - Japanese
    #   'text' : u"Ce est texte généré aléatoirement" # Your SMS Text Message - French
    url="http://foo.com/sms_status/", # URL for callback
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

# Print the message message_uuid
print (response.message_uuid)

# Sample successful output
# db3ce55a-7f1d-11e1-8ea7-1231380bc196

# Print the api_id
print(response.api_id)

# Sample successful output
# db342550-7f1d-11e1-8ea7-1231380bc196