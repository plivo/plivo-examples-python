from flask import Flask, Response
import plivo, plivoxml

app = Flask(__name__)

@app.route('/greet_caller/', methods=['GET', 'POST'])
def greet_caller():
    from_number = request.values.get('From')
    callers = {
        "1111111111": "ABCDEF",
        "2222222222": "VWXYZ",
        "3333333333": "QWERTY",
    }

    response = plivoxml.Response()
    if from_number in callers:
        body = "Hello," + callers[from_number]
    else:
        body = "Hello Stranger!"

    response.addSpeak(body)
    print response.to_xml()
    return Response(str(response), mimetype='text/xml')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

'''
Sample Output
<Response>
    <Speak>Hello,ABCDEF</Speak>
</Response>
'''