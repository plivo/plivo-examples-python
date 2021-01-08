from flask import Flask, request, make_response, url_for
import plivo
from plivo import plivoxml

app = Flask(__name__)

@app.route('/speak/', methods=['GET', 'POST'])
def validate_signature():
    signature = request.headers.get('X-Plivo-Signature-V3', 'signature')
    nonce = request.headers.get('X-Plivo-Signature-V3-Nonce', '12345')
    url = url_for('validate_signature', _external=True)
    auth_token = "your_auth_token"
    method = request.method
    if method == 'GET':
        valid = plivo.utils.validate_v3_signature(
            method, url, nonce, auth_token, signature)
    else:
        params = request.get_json()
        valid = plivo.utils.validate_v3_signature(
            method, url, nonce, auth_token, signature, params)
    print(valid)
    r = plivoxml.ResponseElement()
    speak_params = {
        'loop': '3'
    }
    r.add(plivoxml.SpeakElement("Hello, from Plivo", **speak_params))
    response = make_response(r.to_string())
    response.headers["Content-type"] = "text/xml"
    print(r.to_string())
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)