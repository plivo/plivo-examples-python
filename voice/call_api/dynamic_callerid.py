import plivo, plivoxml

# Set te caller ID using Dial XML

number = "2222222222"
params = {
    'callerId': "1111111111"
}

response = plivoxml.Response()

d = response.addDial(**params)
d.addNumber(number)
print response.to_xml()

# Sample successful output
# <Response>
#   <Dial callerId="1111111111"><Number>2222222222</Number></Dial>
# </Response>

# Set the caller ID using Call API

auth_id = "Your AUTH_ID"
auth_token = "Your Auth_TOKEN"

p = plivo.RestAPI(auth_id, auth_token)

params = {
    'to': '2222222222', # The phone numer to which the all has to be placed
    'from' : '1111111111', # The phone number to be used as the caller id
    'answer_url' : "http://morning-ocean-4669.herokuapp.com/answer/", # The URL invoked by Plivo when the outbound call is answered
    'answer_method' : "GET", # method to invoke the answer_url
}

response = p.make_call(params)

print str(response) 

# Sample successful output
# (201, {
#	u'message': u'call fired', 
#	u'request_uuid': u'85b1d45d-bc12-47f5-89c7-ae4a2c5d5713', 
#	u'api_id': u'ad0e27a8-9008-11e4-b932-22000ac50fac'
#	}
# )