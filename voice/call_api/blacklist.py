from flask import Flask, Response
from flask import request
from plivo import plivoxml

app = Flask(__name__)

@app.route('/screen_call/', methods=['GET', 'POST'])
def screen_call():

    blacklist = ['14156667777','14156667778','14156667779']
    from_number = request.values.get('From')
    response = plivoxml.ResponseElement()
    
    if from_number in blacklist:
        params = {'reason': 'rejected'}
        response.add(plivoxml.HangupElement(**params))
    else:
        response.add(plivoxml.SpeakElement('Hello, how are you today'))
    return Response(response.to_string(), mimetype='application/xml')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

'''
Sample output when From number is in blacklist
<Response>
    <Hangup reason="rejected"/>
</Response>

Sample Output when From number is not in blacklist
<Response>
    <Speak>Hello, how are you today</Speak>
</Response>
'''