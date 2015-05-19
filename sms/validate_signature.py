from flask import Flask, request, make_response
import plivo, plivoxml
import urlparse

app = Flask(__name__)

@app.route('/receive_sms/', methods =['GET','POST'])
def speak():
    signature = request.headers.get('X-Plivo-Signature')
    uri = url_for('speak', _external=True)
    auth_token = "Your AUTH TOKEN"
    url = request.url
    parsed = urlparse.urlparse(url)
    params = dict(urlparse.parse_qsl(parsed.query))
    
    data = dict((key, request.form.getlist(key)[0]) for key in request.form.keys())
    params.update(data)
    valid = plivo.validate_signature(uri,params,signature,auth_token)
    print valid

    # Sender's phone numer
    from_number = request.values.get('From')

    # Receiver's phone number - Plivo number
    to_number = request.values.get('To')

    # The text which was received
    text = request.values.get('Text')

    # Print the message
    print 'Text received: %s - From: %s' % (text, from_number)
    return "Text received"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)