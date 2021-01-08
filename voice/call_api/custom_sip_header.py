import plivo

client = plivo.RestClient("YOUR_AUTH_ID", "YOUR_AUTH_TOKEN")
response = client.calls.create(
    from_="14152224444", # The phone number to be used as the caller id
    to_="14152223333< 14151112222", # The phone numers to which the all has to be placed. The numbers are separated by "<" delimiter.
    answer_url="http://s3.amazonaws.com/static.plivo.com/answer.xml", # The URL invoked by Plivo when the outbound call is answered
    answer_method="GET", # The method used to call the answer_url
    sip_headers="Test=Sample" # List of SIP headers in the form of 'key=value' pairs, separated by commas.
)
print(response)

# Sample Output
# {
#    "api_id":"a3fd14a6-50b7-11eb-b4f1-0242ac110003",
#    "message":"calls fired",
#    "request_uuid":[
#       "7f22731b-ccb3-40fb-b547-96938cb81162"
#    ]
# }

# The SIP header can be seen as a query parameter in the answer_url
# path="/speech/?Direction=outbound&From=1111111111&ALegUUID=5260e820-958c-11e4-b6bf-498d468c930b&BillRate=0.00300&
# To=sip%3Aabcd150105094929%40phone.plivo.com&X-PH-Test=Sample&CallUUID=5260e820-958c-11e4-b6bf-498d468c930b&ALegRequestUUID=2202d0ab-a890-4199-8582-e7a2615cb23b&
# RequestUUID=2202d0ab-a890-4199-8582-e7a2615cb23b&SIP-H-To=%3Csip%3Aabcd150105094929%40phone.plivo.com%3E%3Btag%3D6U9J4.uVHI7KyEKSgD8vrPnAKQoR2QXc&
# CallStatus=in-progress&Event=StartApp" host=http://s3.amazonaws.com/static.plivo.com/ request_id=07c4ae01-65d6-4463-afcd-ebdd9f6812e0 fwd="54.241.2.243" 
# dyno=web.1 connect=2ms service=5ms status=200 bytes=1104
