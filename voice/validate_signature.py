from flask import Flask, request, make_response
import plivo, plivoxml
import urlparse

app = Flask(__name__)

@app.route('/speak/', methods =['GET','POST'])
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

    r = plivoxml.Response()
    speak_params = {
        'loop': '3'
    }
    r.addSpeak("Hello, from Plivo",**speak_params)
    response = make_response(r.to_xml())
    response.headers["Content-type"] = "text/xml"
    print r.to_xml()
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)