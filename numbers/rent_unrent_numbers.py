import plivo

auth_id = "Your AUTH_ID"
auth_token = "Your AUTH_TOKEN"

p = plivo.RestAPI(auth_id, auth_token)

# Search for new number
params = {
        'country_iso': 'US', # The ISO code A2 of the country
        'type' : 'local', # The type of number you are looking for. The possible number types are local, national and tollfree.
        'pattern' : '210', # Represents the pattern of the number to be searched. 
        'region' : 'Texas' # This filter is only applicable when the number_type is local. Region based filtering can be performed.
    }

response = p.search_phone_numbers(params)
#print str(response)

# Sample successful output
# (200, {
#       u'meta': {
#            u'previous': None, 
#            u'total_count': 100, 
#            u'offset': 0, 
#            u'limit': 20, 
#            u'next': u'/v1/Account/MAYMFHYZJKMJG0NJG4OG/PhoneNumber/?limit=20&country_iso=US&pattern=210&region=Texas&offset=20&type=local'
#        }, u'objects': [
#            {
#                u'restriction': None, 
#                u'rate_center': u'SANANTONIO', 
#                u'voice_enabled': True, 
#                u'country': u'UNITED STATES', 
#                u'region': u'Texas, UNITED STATES', 
#                u'restriction_text': None, 
#                u'prefix': u'210', 
#                u'number': u'12109206499', 
#                u'monthly_rental_rate': u'0.80000', 
#                u'voice_rate': u'0.00850', 
#                u'lata': 566, 
#                u'setup_rate': u'0.00000', 
#                u'sms_rate': u'0.00000', 
#                u'type': u'fixed', 
#                u'sms_enabled': True, 
#                u'resource_uri': u'/v1/Account/MAYMFHYZJKMJG0NJG4OG/PhoneNumber/12109206499/'
#            }, {
#                u'restriction': None, 
#                u'rate_center': u'SANANTONIO', 
#                u'voice_enabled': True, 
#                u'country': u'UNITED STATES', 
#                u'region': u'Texas, UNITED STATES', 
#                u'restriction_text': None, 
#                u'prefix': u'210', 
#                u'number': u'12109206500', 
#                u'monthly_rental_rate': u'0.80000', 
#                u'voice_rate': u'0.00850', 
#                u'lata': 566, 
#                u'setup_rate': u'0.00000', 
#                u'sms_rate': u'0.00000', 
#                u'type': u'fixed', 
#                u'sms_enabled': True, 
#                u'resource_uri': u'/v1/Account/MAYMFHYZJKMJG0NJG4OG/PhoneNumber/12109206500/'
#            }
#        ], u'api_id': u'd8692ccc-b66e-11e4-ac1f-22000ac51de6'
#    }
# )

# Buy a phone number
params = {
    'number' : '12109206499' # The phone number
}

response = p.buy_phone_number(params)
print str(response)

# Sample Output
# (201, {
#        u'status': u'fulfilled', 
#        u'message': u'created', 
#        u'numbers': [
#            {
#                u'status': u'Success', 
#                u'number': u'12109206499'
#            }
#        ], u'api_id': u'85201b0a-b670-11e4-b423-22000ac8a2f8'
#    }
# )

# Modify alias of a number
params = {
        'number' : '12109206499', # Number that has to be modified
        'alias' : 'testing' # The textual name given to the number
}

response = p.modify_number(params)
print str(response)

# Sample successful output
# (202, {
#       u'message': u'changed',
#       u'api_id': u'e13fcf9a-8a90-11e4-b423-22000ac8a2f8'
#       }
# )

# Modify the application linked to a number
params = {
        'number' : '12109206499', # Number that has to be modified
        'app_id' : '16638156474000802' # The application id of the application that is to be linked
}

response = p.modify_number(params)
print str(response)

# Sample successful output
# (202, {
#		u'message': u'changed', 
#		u'api_id': u'e78761bc-8f52-11e4-b423-22000ac8a2f8'
#		}
# )

# Unrent a number
params = {
        'number' : '12109206499' # Number that has to be unrented
}

response = p.unrent_number(params)
print str(response)

# Sample successful output
# (204, '')

# Sample unsuccessful output
# (404, {
#		u'api_id': u'7c33ff78-8f53-11e4-b932-22000ac50fac', 
#		u'error': u'not found'
#		}
# )	
