from flask import Flask, request, make_response
import plivo, plivoxml

app = Flask(__name__)

@app.route('/play/', methods=['GET','POST'])
def play_xml():

    # Generate a Play XML with the details of audio file to play during the call

    body = "https://s3.amazonaws.com/plivocloud/Trumpet.mp3"
    r = plivoxml.Response()
    r.addPlay(body)
    ret_resp = make_response(r.to_xml())
    ret_resp.headers["Content-Type"] = "text/xml"
    print r.to_xml()
    return ret_resp

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

# Sample successful output
# <Response>
#	<Play>https://s3.amazonaws.com/plivocloud/Trumpet.mp3</Play>
# </Response>
