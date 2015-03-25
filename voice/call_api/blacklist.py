from flask import Flask, Response
import plivo, plivoxml

app = Flask(__name__)

@app.route('/reject_call/', methods=['GET', 'POST'])
def reject_call():

    blacklist = ['1111111111','2222222222']
    from_number = request.values.get('From')
    print ("From %s") % from_number

    response = plivoxml.Response()

    if from_number in blacklist:
        params = {
            'reason': 'rejected' # Specify the reason for hangup
        }
        response.addHangup(**params)
        print response.to_xml()
    else:
        response.addSpeak('Hello from Plivo')        
        print response.to_xml()
    
    return Response(str(response), mimetype='text/xml')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

'''
Sample output when From number is in blacklist
<Response>
    <Hangup reason="rejected"/>
</Response>

Sample Output when From number is not in blacklist
<Response>
    <Speak>Hello from Plivo</Speak>
</Response>
'''