from flask import Flask, request
import smtplib

app = Flask(__name__)

@app.route("/email_sms/", methods =['GET','POST'])
def receive_sms():
    # Sender's phone number
    from_number = request.values.get('From')
    # Receiver's phone number - Plivo number
    to_number = request.values.get('To')
    # The text which was received on your Plivo number
    text = request.values.get('Text')

    # Print the message
    print ('Message received from %s: %s' % (from_number, text))
    # Send the received SMS to your mail account
    return to_email(text, from_number)

def to_email(text, from_number):
    user_name = 'Your email address'
    password = 'Your password'
    from_ = 'From email address'
    to = ['To email address'] # must be a list
    subject = "SMS from %s" % (from_number)
    body = text

    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (from_, ", ".join(from_), subject, body)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user_name, password)
        server.sendmail(from_, to, message)
        server.close()
        print ('successfully sent the email')
    except:
        print ("failed to send email")
    return "SMS sent to email"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
        

# Sample successful output
# Text received: from: 14152224444 : Hello, from Plivo
# successfully sent the mail
