from flask import Flask, Response, request, url_for
from plivo import plivoxml

# This file will be played when a caller presses 2.
plivo_song = "https://s3.amazonaws.com/plivocloud/music.mp3"
# This is the message that Plivo reads when the caller dials in
ivr_message1 = "Welcome to the Plivo IVR Demo App. Press 1 to listen to a pre recorded text in different languages.  \
                Press 2 to listen to a song."
ivr_message2 = "Press 1 for English. Press 2 for French. Press 3 for Russian"
# This is the message that Plivo reads when the caller does nothing at all
noinput_message = "Sorry, I didn't catch that. Please hangup and try again \
                    later."
# This is the message that Plivo reads when the caller inputs a wrong number.
wronginput_message = "Sorry, it's wrong input."

app = Flask(__name__)

@app.route('/ivr/', methods=['GET','POST'])
def ivr():
    response = plivoxml.ResponseElement()
    getinput_action_url = "http://www.foo.com/firstbranch/"
    response.add(plivoxml.GetInputElement().
        set_action(getinput_action_url).
        set_method('POST').
        set_input_type('dtmf').
        set_digit_end_timeout(5).
        set_redirect(True).add(
            plivoxml.SpeakElement(ivr_message1)))
    response.add(plivoxml.SpeakElement(noinput_message))
    return Response(response.to_string(), mimetype='application/xml')

@app.route('/ivr/firstbranch/', methods=['GET','POST'])
def firstbranch():
    response = plivoxml.ResponseElement()
    digit = request.values.get('Digits')
    if digit == "1":
        # Read out a text.
        getinput_action_url = "http://www.foo.com/secondbranch/"
        response.add(plivoxml.GetInputElement().
            set_action(getinput_action_url).
            set_method('POST').
            set_input_type('dtmf').
            set_digit_end_timeout(5).
            set_redirect(True).add(
                plivoxml.SpeakElement(ivr_message2)))
        response.add(plivoxml.SpeakElement(noinput_message))

    elif digit == "2":
        # Listen to a song
        response.add_play(plivo_song)

    else:
        response.add_speak(wronginput_message)
    return Response(response.to_string(), mimetype='application/xml')

@app.route('/ivr/secondbranch/', methods=['GET','POST'])
def secondbranch():
    response = plivoxml.ResponseElement()
    digit = request.values.get('Digits')

    if digit == "1":
        text = u"This message is being read out in English"
        params = {
            'language': "en-GB",
        }
        response.add_speak(text,**params)

    elif digit == "2":
        text = u"Ce message est lu en français"
        params = {
            'language': "fr-FR",
        }
        response.add_speak(text,**params)

    elif digit == "3":
        text = u"Это сообщение было прочитано в России"
        params = {
            'language': "ru-RU",
        }
        response.add_speak(text,**params)

    else:
        response.add_speak(wronginput_message)
    return Response(response.to_string(), mimetype='application/xml')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

# Sample output
# <Response>
#    <GetDigits action="http://foo.com/response/ivr/" method="POST" numDigits="1" retries="1" timeout="7">
#        <Speak>Welcome to the Plivo IVR Demo App. Press 1 to listen to a pre recorded text in different languages. Press 2 to listen to a song.</Speak>
#    </GetDigits>
#    <Speak>Sorry, I didn't catch that. Please hangup and try again later.</Speak>
# </Response>

# If 1 is pressed, another menu is read out. Following is the generated Speak XML.
# <Response>
#    <GetDigits action="http://foo.com/response/tree/" method="POST" numDigits="1" retries="1" timeout="7">
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
#   <Speak language="ru-RU">Это сообщение было прочитано в России</Speak>
# </Response>

# If 2 is pressed, a music is played. Following is the generated Play XML.
# <Response>
#   <Play>https://s3.amazonaws.com/plivocloud/music.mp3</Play>
# </Response>

