from flask import Flask, request, Response
import plivoxml

app=Flask(__name__)

@app.route('/dial/', methods=['GET','POST'])
def dial():
    
    # When an outbound call is made and then connected different number using Dial element, 
    # you can play a custom caller tone using the dialMusic attribute    
    
    response = plivoxml.Response()
    params = {
        'dialMusic' : "https://morning-ocean-4669.herokuapp.com/custom_tone/"
    }
    d = response.addDial(**params)
    d.addNumber("1111111111")
    print response.to_xml()
    return Response(str(response), mimetype='text/xml')

# Sample Dial XML
# <Response>
#    <Dial dialMusic="https://morning-ocean-4669.herokuapp.com/custom_tone/">
#        <Number>1111111111</Number>
#    </Dial>
# </Response> 

# Play XML is returned on the dialMusic Url

@app.route('/custom_tone/', methods=['GET','POST'])
def custom_tone():

    response = plivoxml.Response()
    response.addPlay("https://s3.amazonaws.com/plivocloud/music.mp3")
    print response.to_xml()
    return Response(str(response), mimetype='text/xml')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8040)

# Sample successful output
# <Response>
#   <Play>https://s3.amazonaws.com/plivocloud/music.mp3</Play>
# </Response>
