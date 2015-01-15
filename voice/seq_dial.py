import plivoxml
from flask import Flask, Response

app=Flask(__name__)

@app.route('/seq_dial/', methods=['GET','POST'])
def dial_status():

    # This example calls out to a list of phone numbers sequentially. 
    # The first call is made to the number in order, with a timeout value to 20s. 
    # If the call is not answered within 20s, Plivo will then dial out to the second number.

    r = plivoxml.Response()
    params = {
        'timeout' : "20", # The duration (in seconds) for which the called party has to be given a ring.
        'action':"https://morning-ocean-4669.herokuapp.com/dial_status/" # Redirect to this URL after leaving Dial.
    }
    d = r.addDial(**params)
    d.addNumber("1111111111")
    d = r.addDial()
    d.addNumber("2222222222")

    print r.to_xml()
    return Response(str(r), mimetype='text/xml')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8040)

# Sample output
# <Response>
#	<Dial action="https://morning-ocean-4669.herokuapp.com/dial_status/" timeout="20">
#		<Number>1111111111</Number>
#	</Dial>
#	<Dial>
#		<Number>2222222222</Number>
#	</Dial>
#</Response>
