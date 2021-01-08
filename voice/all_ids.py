import plivo

client = plivo.RestClient ("YOUR_AUTH_ID", "YOUR_AUTH_TOKEN")
response = client.calls.create(
    from_='14152224444', # The phone number to be used as the caller id
    to_='14152223333', # The phone numer to which the all has to be placed
    answer_url='http://s3.amazonaws.com/static.plivo.com/answer.xml', # The URL invoked by Plivo when the outbound call is answered
    answer_method='GET', # Method used to invoke the answer_url
    )
print ("API ID : %s " % (response.api_id))
print ("Request ID : %s " % (response.request_uuid))

# Sample successful output
# API ID : a14d2070-9505-11e4-b932-22000ac50fac
# Request ID : 85b1d45d-bc12-47f5-89c7-ae4a2c5d5713

# Call UUID is th id of a live call. This ID is returned only after the call is answered.

# Get the details of all live calls
response = client.live_calls.list_ids()
print ("Call UUID : %s " % response['calls'])

# Sample successful output
# Call UUID : ['a60f44dc-926f-11e4-82f5-b559cbfe39b9','af399206-926f-11e4-8b6f-fd067af138be']
