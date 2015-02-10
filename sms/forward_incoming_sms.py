from flask import Flask, request, make_response
import plivo, plivoxml

app = Flask(__name__)

@app.route('/forward_sms/', methods=['GET','POST'])
def inbound_sms():

    # Sender's phone number
    from_number = request.values.get('From')

    # Receiver's phone number - Plivo number
    to_number = request.values.get('To')

    # The text which was received
    text = request.values.get('Text')

    # Print the message
    print 'Text received: %s - From: %s' % (text, from_number)

    # Generate a Message XML with the details of the reply to be sent

    resp = plivoxml.Response()

    # The phone number to which the SMS has to be forwarded
    to_forward = '1111111111'

    body = 'Forwarded message : %s' % (text)
    params = {
    'src' : to_number, # Sender's phone number
    'dst' : to_forward, # Receiver's phone number
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
    app.run(host='0.0.0.0', port=8040, debug=True)

# Sample successful output
# Text received: Hello, from Plivo - From: 3333333333
# <Response>
#       <Message dst="1111111111" src="2222222222" type="sms">Forwarded message : Hello, from Plivo</Message>
# </Response>
