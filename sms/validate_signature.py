from flask import Flask, request, url_for
import plivo

app = Flask(__name__)

@app.route('/receive_sms/', methods =['GET','POST'])
def signature():
    signature = request.headers.get('X-Plivo-Signature-V2')
    nonce = request.headers.get('X-Plivo-Signature-V2-Nonce')
    uri = url_for('signature', _external=True)
    auth_token = "Your_Auth_Token"
    
    output = plivo.utils.validate_signature(uri,nonce,signature,auth_token)
    print(output)

    from_number = request.values.get('From') # Sender's phone numer
    to_number = request.values.get('To') # Receiver's phone number - Plivo number
    text = request.values.get('Text') # The text which was received

    print('Message received - From: %s, To: %s, Text: %s' %(from_number, to_number, text))
    return "Text received"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)