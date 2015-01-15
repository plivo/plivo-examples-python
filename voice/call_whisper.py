import plivoxml
from flask import Flask, request, Response

app=Flask(__name__)

@app.route('/call_whisper/', methods=['GET','POST'])
def call_whisper():
    r = plivoxml.Response()
    params = {
        'confirmSound' : "https://morning-ocean-4669.herokuapp.com/confirm_sound/", # A remote URL fetched with POST HTTP request which must return an 
                                                                                    # XML response with Play, Wait and/or Speak elements only.
        'confirmKey' : "5" # The digit to be pressed by the called party to accept the call.
    }
    d = r.addDial(**params)
    d.addNumber("1111111111")
    d.addNumber("2222222222")
    d.addNumber("3333333333")
    print r.to_xml()
    return Response(str(r), mimetype='text/xml')

@app.route('/confirm_sound/', methods=['GET','POST'])
def confirm_sound():
    r = plivoxml.Response()
    r.addSpeak("Press 5 to answer the call")
    print r.to_xml()
    return Response(str(r), mimetype='text/xml')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8040)

# Sample output
# <Response>
#    <Dial confirmKey="5" confirmSound="ttps://morning-ocean-4669.herokuapp.com/confirm_sound/">
#        <Number>1111111111</Number>
#        <Number>2222222222</Number>
#        <Number>3333333333</Number>
#    </Dial>
# </Response>

# <Response>
#    <Speak>Press 5 to answer the call</Speak>
# </Response>
