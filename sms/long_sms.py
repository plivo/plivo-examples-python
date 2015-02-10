# -*- coding: utf-8 -*-
import plivo

auth_id = "Your AUTH_ID"
auth_token = "Your AUTH_TOKEN"

p = plivo.RestAPI(auth_id, auth_token)

# SMS containing more than 160 standard characters, is automatically split as a long SMS.  
# SMS containing more than 70 Unicode characters, is automatically split as a long SMS.
# Information about split SMSes are sent to the url and are also reported in the Message Logs in the Account Dashboard. 

params = {
    'src': '2222222222', # Sender's phone number
    'dst' : '1111111111', # Receiver's phone Number
#   'text' : u"Ce texte généré aléatoirement peut-être utilisé dans vos maquettes (webdesign, sites internet,livres, affiches...) gratuitement. Ce texte est entièrement libre de droit. N'hésitez pas à faire un lien sur ce site en utilisant l'image ci-dessous ou en faisant un simple lien texte", 
    # Long text in French
    #'text' : u"This randomly generated text can be used in your layout (webdesign , websites, books, posters ... ) for free. This text is entirely free of law. Feel free to link to this site by using the image below or by making a simple text link",
    # Long text in English
    'text' : u"このランダムに生成されたテキストは、自由のためのあなたのレイアウト（ウェブデザイン、ウェブサイト、書籍、ポスター...）で使用することができます。このテキストは、法律の完全に無料です。下の画像を使用して、または単純なテキストリンクを作ることで、このサイトへのリンクフリーです",
    # Long text in Japanese
    'url' : "http://morning-ocean-4669.herokuapp.com/report/", # The URL to which with the status of the message is sent
    'method' : 'GET' # he method used to call the url
}

response = p.send_message(params)

# Prints the complete response
print str(response)

# Sample successful output
#(202, {
#	u'message': u'message(s) queued', 
#	u'message_uuid': [u'dcfc1510-9260-11e4-b1a4-22000ac693b1'], 
#	u'api_id': u'dce8fb42-9260-11e4-b932-22000ac50fac'
#	}
# )

uuid = str(response[1]['message_uuid'][0])
print "Message_uuid : %s " % (uuid)

# Output
# Message_uuid : 2d97bbfe-9262-11e4-9bd8-22000afa12b9

# To get the SMS split units

params1 = {
    'message_uuid': uuid
}

response1 = p.get_message(params1)

print "Your SMS was split into %s units" % response1[1]['units']

# Output for Japanese
# Your SMS was split into 3 units

# Output for English
# Your SMS was split into 2 units

# Output for French
# Your SMS was split into 5 units