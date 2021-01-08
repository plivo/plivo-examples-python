import plivo

client = plivo.RestClient("YOUR_AUTH_ID", "YOUR_AUTH_TOKEN")
response = client.messages.create(
    src="14152224444",  # Sender's phone number with country code
    dst="14152223333< 14151112222",  # Receivers' phone numbers with country code. The numbers are separated by "<" delimiter.
    text="Hello, this is a sample text",  # Your SMS Text Message
)
print(response)

# Sample sucessful output
# {
#    "api_id":"984bc856-9231-11e7-b886-067c5485c240",
#    "message":"message(s) queued",
#    "message_uuid":[
#       "6da4afba-2bcf-4a87-9eff-d2f88577b0f1",
#       "6da384ba-19js-aand-2h3g-r2f8ja0700f1"
#    ]
# }

# Print the message uuid
print(response.message_uuid)

# Sample successful output
#"6da4afba-2bcf-4a87-9eff-d2f88577b0f1",
#"6da384ba-19js-aand-2h3g-r2f8ja0700f1"

# When an invalid number is given as dst parameter, an error will be thrown & message will be sent for that number.

response = client.messages.create(
    src="14152224444",  # Sender's phone number with country code
    dst=" 14152223333< 14151112222",  # Receivers' phone numbers with country code. The numbers are separated by "<" delimiter.
    text="Hello, this is a sample text",  # Your SMS Text Message
)
print(response)

# Sample output
{
   "api_id":"984bc856-9231-11e7-b886-067c5485c240",
   "invalid_number":[
      "14151112222"
   ],
   "message":"message(s) queued",
   "message_uuid":[
      "6da4afba-2bcf-4a87-9eff-d2f88577b0f1",
   ]
}
