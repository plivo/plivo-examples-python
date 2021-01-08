import plivo

client = plivo.RestClient("YOUR_AUTH_ID", "YOUR_AUTH_TOKEN")
response = client.calls.create(
    from_="14152224444", # The phone number to be used as the caller id
    to_="+14152223333<+14151112222", # The phone numers to which the all has to be placed. The numbers are separated by "<" delimiter.
    answer_url="http://s3.amazonaws.com/static.plivo.com/answer.xml", # The URL invoked by Plivo when the outbound call is answered
    answer_method="GET", # The method used to call the answer_url
)
print(response)

# Sample successful output
# {
#    "api_id":"a3fd14a6-50b7-11eb-b4f1-0242ac110003",
#    "message":"calls fired",
#    "request_uuid":[
#       "7f22731b-ccb3-40fb-b547-96938cb81162",
#       "8fe356e1-a9d0-4934-a0bd-34dd37d0dde2"
#    ]
# }