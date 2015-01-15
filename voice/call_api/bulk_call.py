import plivo

auth_id = "Your AUTH_ID"
auth_token = "Your AUTH_TOKEN"

p = plivo.RestAPI(auth_id, auth_token)

params = {
    'to': '2222222222<3333333333', # The phone numers to which the all has to be placed. The numbers are separated by "<" delimiter.
    'from' : '1111111111', # The phone number to be used as the caller id
    'answer_url' : "http://morning-ocean-4669.herokuapp.com/speech/", # The URL invoked by Plivo when the outbound call is answered
    'answer_method' : "GET", # The method used to call the answer_url
}

# Make an outbound call
response = p.make_call(params)

print str(response)

# Sample successful output
# (202, {
#       u'message': u'call fired',
#       u'request_uuid': [
#               u'd7fa180c-9501-11e4-a4d0-3f7813869e0a',
#               u'd7fa180c-9501-11e4-a4d0-3f7813869e1a'
#       ],
#       u'api_id': u'be50302a-9502-11e4-a0ec-fd067af138be'
#       }
# )