from flask import Flask, Response
from plivo import plivoxml

app = Flask(__name__)

@app.route('/forward_call/', methods=['GET', 'POST'])
def forwardcall():

    response = plivoxml.ResponseElement()
    response.add(
        plivoxml.DialElement().add(
            plivoxml.NumberElement('15671234567'))) # call wll be forwarded to this number
    return Response(response.to_string(), mimetype="application/xml")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

# Sample sucessful output
# <Response>
#   <Dial>
#       <Number>15671234567</Number>
#   </Dial>
# </Response>