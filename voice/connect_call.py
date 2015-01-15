from flask import Flask, Response
import plivo, plivoxml

app = Flask(__name__) 

@app.route("/connect/", methods=['GET', 'POST'])
def connect():

    # Generate a Dial XML with the details of the number to call 
   
	body = "Connecting your call.."
	r = plivoxml.Response()
	r.addSpeak(body)
	number = "2222222222"
	d = r.addDial()
	d.addNumber(number)
    print r.to_xml()
    return Response(str(r), mimetype='text/xml')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

# Sample successful output
# <Response>
#   <Speak>Connecting your call..</Speak>
#   <Dial>
#       <Number>2222222222</Number>
#   </Dial>
# </Response>