import plivo, plivoxml
from flask import Flask, request


app = Flask(__name__)

@app.route("/email/", methods =['GET','POST'])
def receive_sms():

    # Sender's phone number
    from_number = request.args.get('From')

    # Receiver's phone number - Plivo number
    to_number = request.args.get('To')

    # The text which was received
    text = request.args.get('Text')

    # Print the message
    print 'Text received: %s - From: %s' % (text, from_number)

    # Send the received SMS to your mail account
    to_email(text)

def to_email(text):
    gmail_user = "Your mail address"
    gmail_pwd = "Your Password"
    FROM = 'From mail address'
    TO = ['To mail address'] #must be a list
    SUBJECT = "Testing sending using gmail"
    TEXT = text

    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"
    return "SMS sent to mail"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

# Sample successful output
# Text received: Hello, from Plivo - From: 2222222222
# successfully sent the mail
