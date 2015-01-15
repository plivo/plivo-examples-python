from flask import Flask, request, make_response
import plivo, plivoxml

app = Flask(__name__)

@app.route('/speak/', methods=['GET','POST'])
def speak_xml():

    # Generate a Speak XML with the details of the text to play on the call.

    body = "Hello, Welcome to Plivo."
    r = plivoxml.Response()
    r.addSpeak(body)
    ret_resp = make_response(r.to_xml())
    ret_resp.headers["Content-Type"] = "text/xml"
    print r.to_xml()
    return ret_resp

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

# Sample successful output
# <Response>
#    <Speak>Hello, Welcome to Plivo.</Speak>
# </Response>