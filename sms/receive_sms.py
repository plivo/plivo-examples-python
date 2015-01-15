import plivo, plivoxml
from flask import Flask, request


app = Flask(__name__)

@app.route("/message/", methods=['GET','POST'])
def receive_sms():

    # Sender's phone numer
    from_number = request.args.get('From')

    # Receiver's phone number - Plivo number
    to_number = request.args.get('To')

    # The text which was received
    text = request.args.get('Text')

    # Print the message
    print 'Text received: %s - From: %s' % (text, from_number)
    return "Text received"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

# Sample successful output
# Text received: Hello, from Plivo - From: 2222222222
