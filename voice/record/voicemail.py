from flask import Flask, Response
import plivo, plivoxml

app = Flask(__name__)

@app.route('/record/',methods=['POST', 'GET'])
def record():

    # Generate a Record XML and ask the caller to leave
    # a message.

    # The recorded file will be sent to the 'action' URL
    record_params = {
        'action': 'https://morning-ocean-4669.herokuapp.com/save_record_url/', # Submit the result of the record to this URL
        'method' : "GET" # HTTP method to submit the action URL
        'maxLength': '30', # Maximum number of seconds to record 
        'transcriptionType' : 'auto', # The type of transcription required
        'transcriptionUrl' : "https://morning-ocean-4669.herokuapp.com/transcription/", # The URL where the transcription while be sent from Plivo
        'transcriptionMethod' : 'GET' # The method used to invoke transcriptionUrl 
    }

    text = "Leave your message after the tone"

    r = plivoxml.Response()
    r.addSpeak(text)
    r.addRecord(**record_params)
    print r.to_xml()
    return Response(str(r), mimetype='text/xml')

# Action URL Example

@app.route("/save_record_url/", methods=['GET'])
def save_record_url():
    return record_file
    if request.method == 'GET':
        print "Record URL : %s" %s (request.args.get('RecordUrl'))
    elif request.method == 'POST':
        print "Record URL : %s" %s (request.form.get('RecordUrl'))
    return Response("OK", mimetype='text/xml')

# Transcription URL Example

@app.route("/transcription/", methods=['GET','POST'])
def transcription():
    if request.method == 'GET':
        print "Transcription is : %s " % (request.args.get('transcription'))
    elif request.method == 'POST':
        print "Transcription is : %s " % (request.form.get('transcription'))
    return Response("OK", mimetype='text/xml')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

# Sample output
# <Response>
#    <Speak>Leave your message after the tone</Speak>
#    <Record action="https://morning-ocean-4669.herokuapp.com/save_record_url/" maxLength="30" method="POST" transcriptionMethod="GET" transcriptionType="auto" 
#        transcriptionUrl="https://morning-ocean-4669.herokuapp.com/transcription/" />
# </Response>

# Record URL : http://s3.amazonaws.com/recordings_2013/xxxxxxx-yyyyy-zzzzzz.mp3 
# Transcription is : Hello