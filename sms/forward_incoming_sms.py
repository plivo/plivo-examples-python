from flask import Flask, request, make_response, Response
import plivo
from plivo import plivoxml

app = Flask(__name__)


@app.route('/forward_sms/', methods=['GET', 'POST'])
def inbound_sms():
    # Sender's phone number
    from_number = request.values.get('From')
    # Receiver's phone number - Plivo number
    to_number = request.values.get('To')
    # The text which was received
    text = request.values.get('Text')
    # Print the message
    print('Message received - From: %s, To: %s, Text: %s' %(from_number, to_number, text))

    # The phone number to which the SMS has to be forwarded
    to_forward = '+14152223333'

    # send the details to generate an XML
    response = plivoxml.ResponseElement()
    response.add(
        plivoxml.MessageElement(
            text,  # The text which was received
            src=to_number,  # Sender's phone number
            dst=to_forward,  # Receiver's phone Number
            type='sms',
            callback_url='http://foo.com/sms_status/',
            callback_method='POST'))
    print(response.to_string())  # Prints the XML
    # Returns the XML
    return Response(response.to_string(), mimetype='application/xml')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

# Sample successful output
# Message received: From: 3333333333, To:14152223333, Text: Hello, from Plivo
# <Response>
#       <Message dst="+14152223333" src="3333333333" type="sms">Hello, from Plivo</Message>
# </Response>
