from flask import Flask, Response, request
from plivo import plivoxml

app = Flask(__name__)

@app.route('/greet_caller/', methods=['GET', 'POST'])
def greet_caller():
    from_number = request.values.get('From')
    callers = {
        "1111111111": "ABCDEF",
        "2222222222": "VWXYZ",
        "3333333333": "QWERTY",
        }
        
    if from_number in callers:
        body = "Hello,"+callers[from_number]
    else:
        body = "Hello Stranger!"

    response = (plivoxml.ResponseElement()
        .add(plivoxml.SpeakElement(body)))
    return Response(response.to_string(), mimetype="application/xml")
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

'''
Sample Output
<Response>
    <Speak>Hello,ABCDEF</Speak>
</Response>
'''