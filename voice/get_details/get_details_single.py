import plivo

client = plivo.RestClient("YOUR_AUTH_ID", "YOUR_AUTH_TOKEN")

response = client.calls.get(
    call_uuid="10f0cb68-7533-45ed-acb5-87ceac29ee48",  # The ID of the call
)
print(response)

# Sample successful output
# {
#    "answer_time":"2015-07-26 15:45:02+05:30",
#    "api_id":"06ae0f8f-dc72-11e5-b56c-22000ae90795",
#    "bill_duration":924,
#    "billed_duration":960,
#    "call_direction":"outbound",
#    "call_duration":924,
#    "call_uuid":"10f0cb68-7533-45ed-acb5-87ceac29ee48",
#    "end_time":"2015-07-26 15:45:14+05:30",
#    "from_number":"+14158572518",
#    "initiation_time":"2015-07-26 15:44:49+05:30",
#    "parent_call_uuid":null,
#    "resource_uri":"/v1/Account/MAXXXXXXXXXXXXXXXXXX/Call/10f0cb68-7533-45ed-acb5-87ceac29ee48/",
#    "to_number":"14153268174",
#    "total_amount":"0.13600",
#    "total_rate":"0.00850",
#    "hangup_cause_name":"End Of XML Instructions",
#    "hangup_cause_code":4010,
#    "hangup_source":"Plivo"
# }