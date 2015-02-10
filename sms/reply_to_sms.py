from flask import Flask, request, make_response
import plivo, plivoxml

app = Flask(__name__)

@app.route('/reply_to_sms/',methods=['GET','POST'])
def inbound_sms():

    # Sender's phone number
    from_number = request.values.get('From')

    # Receiver's phone number - Plivo number
    to_number = request.values.get('To')

    # The text which was received
    text = request.values.get('Text')

    # Print the message
    print 'Text received: %s - From: %s' % (text, from_number)

    # Generate a Message XML with the details of the reply to be sent.

    resp = plivoxml.Response()

    body = 'Thank you for your message'
    params = {
    'src' : to_number, # Sender's phone number
    'dst' : from_number, # Receiver's phone Number
    'callbackUrl': "http://morning-ocean-4669.herokuapp.com/report/", # URL that is notified by Plivo when a response is available and to which the response is sent
    'callbackMethod' : "GET" # The method used to notify the callbackUrl
    }

    # Message added
    resp.addMessage(body, **params)

    ret_response = make_response(resp.to_xml())
    ret_response.headers["Content-type"] = "text/xml"

    # Prints the XML
    print resp.to_xml()
    # Returns the XML
    return ret_response


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

# Sample successful output
# Text received: Hello, from Plivo - From: 2222222222
#<Response>
#   <Message callbackMethod="GET" callbackUrl="http://morning-ocean-4669.herokuapp.com/report/" dst="2222222222" src="1111111111">Thank you for your message</Message>
#</Response>
