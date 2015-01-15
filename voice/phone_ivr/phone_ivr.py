#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, Response, request, url_for
import plivoxml

# This file will be played when a caller presses 2.
PLIVO_SONG = "https://s3.amazonaws.com/plivocloud/music.mp3"

# This is the message that Plivo reads when the caller dials in
IVR_MESSAGE1 = "Welcome to the Plivo IVR Demo App. Press 1 to listen to a pre recorded text in different languages.  \
                Press 2 to listen to a song."

IVR_MESSAGE2 = "Press 1 for English. Press 2 for French. Press 3 for Russian"
# This is the message that Plivo reads when the caller does nothing at all
NO_INPUT_MESSAGE = "Sorry, I didn't catch that. Please hangup and try again \
                    later."

# This is the message that Plivo reads when the caller inputs a wrong number.
WRONG_INPUT_MESSAGE = "Sorry, it's wrong input."

app = Flask(__name__)

@app.route('/response/ivr/', methods=['GET','POST'])
def ivr():
    response = plivoxml.Response()
    if request.method == 'GET':
        # GetDigit XML Docs - http://plivo.com/docs/xml/getdigits/
        getdigits_action_url = url_for('ivr', _external=True)
        getDigits = plivoxml.GetDigits(action=getdigits_action_url,
        method='POST', timeout=7, numDigits=1,
        retries=1)

        getDigits.addSpeak(IVR_MESSAGE1)
        response.add(getDigits)
        response.addSpeak(NO_INPUT_MESSAGE)
        print response.to_xml()
        return Response(str(response), mimetype='text/xml')

    elif request.method == 'POST':
        digit = request.form.get('Digits')
        print digit
        if digit == "1":
            # Read out a text.
            getdigits_action_url1 = url_for('tree', _external=True)
            getDigits1 = plivoxml.GetDigits(action=getdigits_action_url1,
            method='POST', timeout=7, numDigits=1,
            retries=1)
            getDigits1.addSpeak(IVR_MESSAGE2)
            response.add(getDigits1)    
            response.addSpeak(NO_INPUT_MESSAGE)

        elif digit == "2":
            # Listen to a song
            response.addPlay(PLIVO_SONG)
        
        else:
            response.addSpeak(WRONG_INPUT_MESSAGE)

        print response.to_xml()
        return Response(str(response), mimetype='text/xml')

@app.route('/response/tree/', methods=['GET','POST'])
def tree():
    response = plivoxml.Response()
    digit = request.form.get('Digits')

    if digit == "1":
        text = u"This message is being read out in English"
        params = {
            'language': "en-GB",
        }
        response.addSpeak(text,**params)

    elif digit == "2":
        text = u"Ce message est lu en français"
        params = {
            'language': "fr-FR",
        }
        response.addSpeak(text,**params)

    elif digit == "3":
        text = u"Это сообщение было прочитано в России"
        params = {
            'language': "ru-RU",
        }
        response.addSpeak(text,**params)

    else:
        response.addSpeak(WRONG_INPUT_MESSAGE)

    print response.to_xml()
    return Response(str(response), mimetype='text/xml')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

# Sample output
# <Response>
#    <GetDigits action="http://morning-ocean-4669.herokuapp.com/response/ivr/" method="POST" numDigits="1" retries="1" timeout="7">
#        <Speak>Welcome to the Plivo IVR Demo App. Press 1 to listen to a pre recorded text in different languages. Press 2 to listen to a song.</Speak>
#    </GetDigits>
#    <Speak>Sorry, I didn't catch that. Please hangup and try again later.</Speak>
# </Response>

# If 1 is pressed, another menu is read out. Following is the generated Speak XML.
# <Response>
#    <GetDigits action="http://morning-ocean-4669.herokuapp.com/response/tree/" method="POST" numDigits="1" retries="1" timeout="7">
#        <Speak>Press 1 for English. Press 2 for French. Press 3 for Russian</Speak>
#    </GetDigits>
#    <Speak>Sorry, I didn't catch that. Please hangup and try again later.</Speak>
# </Response>

# If 1 is pressed, the English text is read out. Following is the generated Speak XML.
# <Response>
#   <Speak language="en-GB">This message is being read out in English</Speak>
# </Response>

# If 2 is pressed, the French text is read out. Following is the generated Speak XML.
# <Response>
#   <Speak language="fr-FR">Ce message est lu en fran&amp;#231;ais</Speak>
# </Response>

# If 3 is pressed, the Russian text is read out. Following is the generated Speak XML.
# <Response>
#   <Speak language="ru-RU">&amp;#1069;&amp;#1090;&amp;#1086; &amp;#1089;&amp;#1086;&amp;#1086;&amp;#1073;&amp;#1097;&amp;#1077;&amp;#1085;&amp;#1080;&amp;#1077; 
#        &amp;#1073;&amp;#1099;&amp;#1083;&amp;#1086; &amp;#1087;&amp;#1088;&amp;#1086;&amp;#1095;&amp;#1080;&amp;#1090;&amp;#1072;&amp;#1085;&amp;#1086; &amp;#1074; 
#        &amp;#1056;&amp;#1086;&amp;#1089;&amp;#1089;&amp;#1080;&amp;#1080;
#   </Speak>
# </Response>

# If 2 is pressed, a music is played. Following is the generated Play XML.
# <Response>
#   <Play>https://s3.amazonaws.com/plivocloud/music.mp3</Play>
# </Response>

