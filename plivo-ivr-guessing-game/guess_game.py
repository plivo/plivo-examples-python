from flask import Flask, url_for, Response, request
from plivo import plivoxml
import plivo
import random
import os

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    response = plivoxml.ResponseElement()
    response.add(
        plivoxml.GetDigitsElement(
            action="/main_menu_response",
            method="POST",
            timeout="4",
            num_digits="4",
            retries="1",
        )
    )
    response.add(plivoxml.SpeakElement("Hello, welcome to Plivo guessing game app!"))
    response.add(plivoxml.SpeakElement("To play the game Press 1"))
    response.add(plivoxml.SpeakElement("To learn how to play Press 2"))
    response.add(plivoxml.SpeakElement("You can end this call at any time."))

    return Response(response.to_string(), mimetype='application/xml')

# Output
# <Response>
#   <GetDigits action="/main_menu_response" method="POST" timeout="4" numDigits="4" retries="1"/>
#   <Speak>Hello, welcome to Plivo guessing game app!</Speak>
#   <Speak>To play the game Press 1</Speak>
#   <Speak>To learn how to play Press 2</Speak>
#   <Speak>You can end this call at any time.</Speak>
# </Response>

def exit_sequence(msg="Oops! There was an error!"):
    response = plivoxml.ResponseElement()
    response.add(plivoxml.HangupElement(schedule=10, reason='rejected'))
    response.add(
    plivoxml.SpeakElement('We did not receive a valid response. We will hangup now.'))

    return Response(response.to_string(), mimetype='application/xml')

# Output
# <Response>
#   <Hangup reason="rejected" schedule="10"/>
#   <Speak>We did not receive a valid response. We will hangup now.</Speak>
# </Response>


@app.route('/main_menu_response', methods=['POST',])
def mm_response():
    post_args = request.form
    print (post_args)
    print (request.data)
    response = plivo.Response()
    input_digit = post_args.get('Digits', None)
    if input_digit != "1" and input_digit != "2":
        return exit_sequence()
    else:
        if input_digit == "1":
            absolute_action_url = url_for('play_game', _external=True)
            response.add(plivoxml.RedirectElement(absolute_action_url,method='POST'))
            return Response(response.to_string(), mimetype='application/xml')
        else:
            absolute_action_url = url_for('how_to_play', _external=True)
            response.add(plivoxml.RedirectElement(absolute_action_url,method='POST'))
            return Response(response.to_string(), mimetype='application/xml')


@app.route('/play_game', methods=['POST',])
def play_game():
    if not request.args.get('guesses', None):
        secret = random.randint(1, 100)
        guesses = 10

        response = plivoxml.ResponseElement()
        absolute_action_url = url_for('play_game', _external=True,
                                      **{'secret': str(secret),
                                         'guesses': str(guesses)})
        
        response.add(
            plivoxml.GetDigitsElement(
                action=absolute_action_url,
                method="POST",
                timeout="10",
                num_digits="4",
                retries="1",)
        .add(
            plivoxml.SpeakElement(
                "I have thought of a secret number between one and one hundred. You have ten guesses to find it!")
                ).add(plivoxml.SpeakElement("You can make your guess now."))
                )
        return Response(response.to_string(), mimetype='application/xml')
    else:
        secret = int(request.args.get('secret', '0'))
        guesses = int(request.args.get('guesses', '0')) - 1
        absolute_action_url = url_for('play_game', _external=True,
                                      **{'secret': str(secret),
                                         'guesses': str(guesses)})

        input_num = request.form.get('Digits', "0")
        response = plivoxml.ResponseElement()
        try:
            input_num = int(input_num)
        except ValueError as e:
            print (e)
            return exit_sequence()

        if input_num == secret:
            response.add(plivoxml.SpeakElement("Congratulations! {} is the right number!"
                              " You have guessed"
                              " it in {} guesses - your score is {}.".format(secret, 10 - guesses, guesses + 1)))
            response.add(plivoxml.WaitElement(None).set_length(2))
            response.add(plivoxml.HangupElement())
            return Response(response.to_string(), mimetype='application/xml')
        else:
            if input_num > secret:
                answer = "Sorry, you guessed %d. The secret is lesser."
            else:
                answer = "Sorry, you guessed %d. The secret is greater."
            response.add(plivoxml.SpeakElement(answer+input_num))
            if guesses > 0:
                response.add(
                    plivoxml.GetDigitsElement(action=absolute_action_url, method='POST',timeout='10',num_digits='4',retries='1').add(
                        plivoxml.SpeakElement("You have {} guesses remaining! Guess again!".format(guesses))))
            else:
                response.add(plivoxml.WaitElement (None).set_length (1))
                response.add(plivoxml.SpeakElement('Sorry, you dont have any remaining guesses. The secret was {}' .format(secret)))
                response.add(plivoxml.HangupElement())
            return Response(response.to_string(), mimetype='application/xml')


@app.route('/how_to_play', methods=['POST'])
def how_to_play():
    response = plivoxml.ResponseElement()
    response.add(plivoxml.SpeakElement('I will think of a secret number that you will have to guess.'))
    response.add(plivoxml.SpeakElement('The number will be between one and one hundred.'))
    response.add(plivoxml.SpeakElement('To make your guess, just dial the digits and end with the hash sign.'))
    response.add(plivoxml.SpeakElement('For each wrong guess, I will tell you if you guessed lesser of greater.'))
    response.add(plivoxml.SpeakElement('You will have a maximum of ten chances to guess the number.'))
    response.add(plivoxml.WaitElement(None).set_length(6))
    response.add(plivoxml.SpeakElement('You will now be transferred to the main menu.'))

    abs_red_url = url_for('index', _external=True)
    response.add(plivoxml.RedirectElement(abs_red_url))

    return Response(response.to_string(), mimetype='application/xml')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
