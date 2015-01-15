import plivoxml
from flask import Flask, Response

app = Flask(__name__)

# Example for Basic Wait

@app.route('/basic_wait/', methods=['GET','POST'])
def basic_wait():
    r = plivoxml.Response()
    r.addSpeak("I will wait for 10 seconds")
    params = {
	    'length': "10" # Time to wait in seconds
    }
    r.addWait(**params)
    r.addSpeak("I just waited 10 seconds")
    print r.to_xml()
    return Response(str(r), mimetype='text/xml')

# Sample Wait XML
# <Response>
#    <Speak>I will wait for 10 seconds</Speak>
#    <Wait length="10" />
#    <Speak>I just waited 10 seconds</Speak>
# </Response>

# Example for Delayed Call Answer

@app.route('/delayed_wait/', methods=['GET','POST'])
def delayed_wait():
    r = plivoxml.Response()
    params = {
	    'length': "10" # Time to wait in seconds
    }
    r.addWait(**params)
    r.addSpeak("Hello")
    print r.to_xml()
    return Response(str(r), mimetype='text/xml')

# Sample Wait XML
# <Response>
#    <Wait length="10" />
#    <Speak>Hello</Speak>
# </Response>

# Example for Beep Detection

@app.route('/beep_det/', methods=['GET','POST'])
def beep_det():
    r = plivoxml.Response()
    params = {
	    'length': "100", # Time to wait in seconds
	    'beep': "true"
    }
    r.addWait(**params)
    r.addSpeak("Hello")
    print r.to_xml()
    return Response(str(r), mimetype='text/xml')

# Sample Wait XML
# <Response>
#    <Wait length="10" beep="true" />
#    <Speak>Hello</Speak>
# </Response>

if __name__=='__main__':
	app.run(host='0.0.0.0',debug='True')

