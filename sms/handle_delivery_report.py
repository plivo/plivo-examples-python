import plivo, plivoxml
from flask import Flask, request

app = Flask(__name__)

@app.route("/report/", methods=['GET','POST'])
def report():

    # Sender's phone number
    from_number = request.args.get('From')

    # Receiver's phone number - Plivo number
    to_number = request.args.get('To')

    # Status of the message
    status = request.args.get('Status')

    # Message UUID
    uuid = request.args.get('MessageUUID')

    # Prints the status and messageuuid
    print "From : %s To : %s Status : %s MessageUUID : %s" % (from_number, to_number, status,uuid)
    return "Delivery reported"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

# Sample successful output
# From : 2222222222 To : 1111111111 Status : delivered MessageUUID : 53e6526a-8a7a-11e4-a77d-22000ae383ea

# Possible values for message status - "queued", "sent", "failed", "delivered", "undelivered" or "rejected"
