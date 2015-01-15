import plivoxml
from flask import Flask, request, Response

app=Flask(__name__)

# Simultaneous dialing is useful when there are SIP users and numbers that you want to dial. 
# The first call that connects will cancel all other tries.

@app.route('/call_hunting/', methods=['GET','POST'])
def call_hunting():
    r = plivoxml.Response()
    d = r.addDial(**params)
    d.addUser("sip:abcd1234@phone.plivo.com")
    d.addNumber("2222222222")
    d.addNumber("3333333333")
    print r.to_xml()
    return Response(str(r), mimetype='text/xml')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

# Sample Dial XML output
# <Response>
#    <Speak>Dialing</Speak>
#    <Dial>
#       <User>sip:ramya150105094929@phone.plivo.com</User>
#        <Number>2222222222</Number>
#        <Number>3333333333</Number>
#    </Dial>
# </Response>