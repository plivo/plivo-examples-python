import plivo

client = plivo.RestClient("YOUR_AUTH_ID", "YOUR_AUTH_TOKEN")

# To record a call
response = client.calls.record(
    call_uuid="3a2e4c90-dcee-4931-8a59-f123ab507e60",  # ID of the call
    time_limit="40",  # Max recording duration in seconds
    callback_url="http://www.foo.com/save_record_url/",  # The URL invoked by the API when the recording ends
    callback_mathod="GET",  # The method which is used to invoke the callback_url
    transcription_type="auto",  # The type of transcription required
    transcription_url="http://www.foo.com/Transcription/",  # The URL where the transcription while be sent from Plivo
    transcription_method="GET",  # The method used to invoke transcriptionUrl
)
print(response)

# Sample output
# {
#   "url": "http://s3.amazonaws.com/recordings_2013/48dfaf60-3b2a-11e3.mp3",
#   "message": "call recording started",
#   "recording_id": "48dfaf60-3b2a-11e3",
#   "api_id": "c7b69074-58be-11e1-86da-adf28403fe48"
# }


# To stop recording a call

response = client.calls.record_stop(
    call_uuid="3a2e4c90-dcee-4931-8a59-f123ab507e60",  # ID of the call
)
print(response)

# Sample output
# No ouput

# To record a conference call

response = client.conferences.record(
    conference_name="testing",  # The conference nam
    callback_url="https://www.foo.com/save_record_url/",  # The URL invoked by the API when the recording ends
    callback_method="GET",  # The method which is used to invoke the callback_url
)
print(response)

# To stop recording a conference call

response = client.conferences.record_stop(
    conference_name="testing",  # The conference name
)
print(response)

# Sample output
# No ouput