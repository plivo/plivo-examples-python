import plivo

auth_id = "Your AUTH_ID"
auth_token = "Your AUTH_TOKEN"

p = plivo.RestAPI(auth_id, auth_token)


# Get number group details
params = {
        'group_id' : '86930523496041'
}

response = p.get_number_group_details(params)
print str(response)

# Sample successful output
# (200, {
#               u'stock': 41,
#               u'voice_enabled': True,
#               u'region': u'Texas, UNITED STATES',
#               u'voice_rate': u'0.00850',
#               u'api_id': u'3dbe4446-8a90-11e4-b153-22000abcaa64',
#               u'prefix': u'214',
#               u'sms_rate': u'0.00000',
#               u'number_type': u'local',
#               u'setup_rate': u'0.00000',
#               u'rental_rate': u'0.80000',
#               u'group_id': u'86930523496041',
#               u'sms_enabled': True,
#               u'resource_uri': u'/v1/Account/XXXXXXXXXXXX/AvailableNumberGroup/86930523496041/'
#       }
# )

# Search number group
params = {
        'country_iso': 'US', # The ISO code A2 of the country
        'number_type' : 'local', # The type of number you are looking for. The possible number types are local, national and tollfree.
        'prefix' : '21', # Represents the area code of the number for a local number
        'region' : 'Texas' # This filter is only applicable when the number_type is local. Region based filtering can be performed.
        }
response = p.get_number_group(params)
print str(response)

# Sample successful output
# (200, {
#       u'meta': {
#               u'previous': None,
#               u'total_count': 2,
#               u'offset': 0,
#               u'limit': 20,
#               u'next': None
#       },
#       u'objects': [
#               {
#                       u'stock': 100,
#                       u'voice_enabled': True,
#                       u'region': u'Texas, UNITED STATES',
#                       u'voice_rate': u'0.00850',
#                       u'prefix': u'210',
#                       u'sms_rate': u'0.00000',
#                       u'number_type': u'local',
#                       u'setup_rate': u'0.00000',
#                       u'rental_rate': u'0.80000',
#                       u'group_id': u'10194491733193',
#                       u'sms_enabled': True, u'resource_uri':
#                       u'/v1/Account/XXXXXXXXXXXX/AvailableNumberGroup/10194491733193/'
#               },
#               {
#                       u'stock': 41,
#                       u'voice_enabled': True,
#                       u'region': u'Texas, UNITED STATES',
#                       u'voice_rate': u'0.00850',
#                       u'prefix': u'214',
#                       u'sms_rate': u'0.00000',
#                       u'number_type': u'local',
#                       u'setup_rate': u'0.00000',
#                       u'rental_rate': u'0.80000',
#                       u'group_id': u'86930523496041',
#                       u'sms_enabled': True,
#                       u'resource_uri': u'/v1/Account/XXXXXXXXXXXX/AvailableNumberGroup/86930523496041/'
#               }
#       ],
#       u'api_id': u'ea20ecd6-8a8e-11e4-ac1f-22000ac51de6'
#       }
# )
