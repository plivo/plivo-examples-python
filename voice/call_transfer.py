import plivo
from flask import Flask, Response

app=Flask(__name__)

@app.route('/call_transfer/', methods=['GET','POST'])
def call_transfer():
    r = plivoxml.Response()
    r.addSpeak("Please wait while your call is being transferred")
    r.addRedirect("https://morning-ocean-4669.herokuapp.com/connect/")
    print r.to_xml()
    return Response(str(r), mimetype='text/xml')


@app.route("/connect/", methods=['GET', 'POST'])
def connect():
    params = {
        'action' : "https://morning-ocean-4669.herokuapp.com/dial_status/",
        'method' : "GET",
        'redirect' : "true"
    }
    body = "Connecting your call.."
    r = plivoxml.Response()
    r.addSpeak(body)
    number = "1111111111"
    d = r.addDial()
    d.addNumber(number)
    print r.to_xml()
    return Response(str(response), mimetype='text/xml')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

# Sample output for Redirect XML
# <Response>
#    <Speak>Please wait while you call is being transferred</Speak>
#    <Redirect>https://morning-ocean-4669.herokuapp.com/connect/</Redirect>
#</Response>

# Sample output for Dial XML
# <Response>
#    <Speak>Connecting your call..</Speak>
#    <Dial>
#        <Number>1111111111</Number>
#    </Dial>
#</Response>
