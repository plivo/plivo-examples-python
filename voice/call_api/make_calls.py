import plivo

client = plivo.RestClient('YOUR_AUTH_ID','YOUR_AUTH_TOKEN')
response = client.calls.create(
    from_='14152224444', # The phone number to be used as the caller id
    to_='+14152223333', # The phone numer to which the all has to be placed
    answer_url='http://s3.amazonaws.com/static.plivo.com/answer.xml', # The URL invoked by Plivo when the outbound call is answered
    answer_method='GET', # The method used to call the answer_url
    )
print(response)

# Sample successful output for Synchronous Request
# {
#    "message":"call fired",
#    "request_uuid":"9834029e-58b6-11e1-b8b7-a5bd0e4e126f",
#    "api_id":"97ceeb52-58b6-11e1-86da-77300b68f8bb"
# }