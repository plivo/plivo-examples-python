#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, make_response
import plivo, plivoxml

app = Flask(__name__)

@app.route('/speech/', methods=['GET','POST'])
def speak_xml():

    # Generate a Speak XML with the details of the text to play on the call.
    body1 = u'This is English!'
    params1 = {  
        'language': "en-GB", 
        'voice': "MAN"
    }
    r = plivoxml.Response()
    r.addSpeak(body1, **params1)
    body2 = u'Ce texte généré aléatoirement peut-être utilisé dans vos maquettes'
    params2 = {
        'language': "fr-FR"
    }
    r.addSpeak(body2, **params2)
    body3 = u'Это случайно сгенерированный текст может быть использован в макете'
    params3 = {
        'language': "ru-RU",
        'voice' : "MAN"
    }
    r.addSpeak(body3, **params3)
    ret_resp = make_response(r.to_xml())
    ret_resp.headers["Content-Type"] = "text/xml"
    print r.to_xml()
    return ret_resp

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

# Sample successful output
# <Response>
#    <Speak language="en-GB" voice="MAN">This is a randomly generated text can be used in your layout</Speak>
#    <Speak language="fr-FR">Ce est texte g&amp;#233;n&amp;#233;r&amp;#233; al&amp;#233;atoirement peut-&amp;#234;tre utilis&amp;#233; dans vos maquettes</Speak>
#    <Speak language="ru-RU">&amp;#1069;&amp;#1090;&amp;#1086; &amp;#1089;&amp;#1083;&amp;#1091;&amp;#1095;&amp;#1072;&amp;#1081;&amp;#1085;&amp;#1086; &amp;#1089;&amp;#1075;&amp;#1077;&amp;#1085;&amp;#1077;&amp;#1088;&amp;#1080;&amp;#1088;&amp;#1086;&amp;#1074;&amp;#1072;&amp;#1085;&amp;#1085;&amp;#1099;&amp;#1081; &amp;#1090;&amp;#1077;&amp;#1082;&amp;#1089;&amp;#1090; &amp;#1084;&amp;#1086;&amp;#1078;&amp;#1077;&amp;#1090; &amp;#1073;&amp;#1099;&amp;#1090;&amp;#1100; &amp;#1080;&amp;#1089;&amp;#1087;&amp;#1086;&amp;#1083;&amp;#1100;&amp;#1079;&amp;#1086;&amp;#1074;&amp;#1072;&amp;#1085; &amp;#1074; &amp;#1084;&amp;#1072;&amp;#1082;&amp;#1077;&amp;#1090;&amp;#1077;</Speak>
# </Response>