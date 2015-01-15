import plivo

auth_id = "Your AUTH_ID"
auth_token = "Your AUTH_TOKEN"

p = plivo.RestAPI(auth_id, auth_token)

params = {
	'country_iso' : "GB" # The 2 digit country ISO code.
}

response = p.pricing(params)
print str(response)

# Sample successful output
# (200, {
#	u'country': u'Angola', 
#	u'api_id': u'f2c941e8-9507-11e4-96e3-22000abcb9af', 
#	u'country_code': 244, 
#	u'country_iso': u'AO', 
#	u'message': {
#		u'inbound': {
#			u'rate': None
#		}, 
#		u'outbound': {
#			u'rate': u'0.00880'
#		}, 
#		u'outbound_networks_list': [
#			{
#				u'rate': u'0.00880', 
#				u'group_name': u'Angola - All'
#			}
#		]
#	}, 
#	u'voice': {
#		u'inbound': {
#			u'ip': {
#				u'rate': u'0.00300'
#			}, 
#			u'local': {
#				u'rate': None
#			}, 
#			u'tollfree': {
#				u'rate': None
#			}
#		}, 
#		u'outbound': {
#			u'ip': {
#				u'rate': u'0.00300'
#			}, 
#			u'local': {
#				u'rate': u'0.09260'
#			}, 
#			u'tollfree': {
#				u'rate': None
#			}, 
#			u'rates': [
#				{
#					u'prefix': [
#						u'24491', 
#						u'24492', 
#						u'24493', 
#						u'24494'
#					], 
#					u'rate': u'0.09260'
#				}, 
#				{
#					u'prefix': [
#						u'244'
#					], 
#					u'rate': u'0.10030'
#				}
#			]
#		}
#	}, 
#	u'phone_numbers': {
#		u'local': {
#			u'rate': None
#		}, 
#		u'tollfree': {
#			u'rate': None
#		}
#	}
# }
# )