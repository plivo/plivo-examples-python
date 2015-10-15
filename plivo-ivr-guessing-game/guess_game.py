from flask import Flask, url_for, Response, request

app = Flask(__name__)

import plivoxml as plivo
import random
import os

@app.route('/', methods=['POST', 'GET'])
def index():
    response = plivo.Response()
    response.addSpeak(body="Hello, welcome to Plivo's "
                      "guessing game app!")
    response.addWait(length=2)

    absolute_action_url = url_for('mm_response', _external=True)
    getDigits = plivo.GetDigits(action=absolute_action_url, method='POST',
                                timeout=4, numDigits=4, retries=1)
    getDigits.addSpeak(body='To play the game Press 1')
    getDigits.addWait(length=1)
    getDigits.addSpeak(body='To learn how to play Press 2')
    getDigits.addWait(length=1)
    getDigits.addSpeak(body='You can end this call at any time.')

    response.add(getDigits)

    return Response(str(response), mimetype='text/xml')


def exit_sequence(msg="Oops! There was an error!"):
    response = plivo.Response()
    response.addSpeak("We did not receive a valid response. We will hangup now.")
    response.addHangup()
    return Response(str(response), mimetype='text/xml')


@app.route('/main_menu_response', methods=['POST',])
def mm_response():
    post_args = request.form
    print post_args
    print request.data
    response = plivo.Response()
    input_digit = post_args.get('Digits', None)
    if input_digit != "1" and input_digit != "2":
        return exit_sequence()
    else:
        if input_digit == "1":
            absolute_action_url = url_for('play_game', _external=True)
            response.addRedirect(body=absolute_action_url, method='POST')
            return Response(str(response), mimetype='text/xml')
        else:
            absolute_action_url = url_for('how_to_play', _external=True)
            response.addRedirect(body=absolute_action_url, method='POST')
            return Response(str(response), mimetype='text/xml')


@app.route('/play_game', methods=['POST',])
def play_game():
    if not request.args.get('guesses', None):
        secret = random.randint(1, 100)
        guesses = 10

        response = plivo.Response()
        absolute_action_url = url_for('play_game', _external=True,
                                      **{'secret': str(secret),
                                         'guesses': str(guesses)})
        getDigits = plivo.GetDigits(action=absolute_action_url, method='POST',
                                    timeout=10, numDigits=4, retries=1)
        getDigits.addSpeak(body="I have thought of a secret number between "
                           "one and one hundred. "
                           "You have ten guesses to find it!")
        getDigits.addSpeak(body="You can make your guess now.")
        response.add(getDigits)
        return Response(str(response), mimetype='text/xml')
    else:
        secret = int(request.args.get('secret', '0'))
        guesses = int(request.args.get('guesses', '0')) - 1
        absolute_action_url = url_for('play_game', _external=True,
                                      **{'secret': str(secret),
                                         'guesses': str(guesses)})

        input_num = request.form.get('Digits', "0")
        response = plivo.Response()
        try:
            input_num = int(input_num)
        except ValueError, e:
            print e
            return exit_sequence()

        if input_num == secret:
            response.addSpeak("Congratulations! %d is the right number!"
                              " You have guessed"
                              " it in %d guesses - your score is %d." %
                              (secret, 10 - guesses, guesses + 1))
            response.addWait(length=2)
            response.addHangup()
            return Response(str(response), mimetype='text/xml')
        else:
            if input_num > secret:
                answer = "Sorry, you guessed %d. The secret is lesser."
            else:
                answer = "Sorry, you guessed %d. The secret is greater."
            response.addSpeak(answer % (input_num))
            if guesses > 0:
                getDigits = plivo.GetDigits(action=absolute_action_url,
                                            method='POST',
                                            timeout=10, numDigits=4,
                                            retries=1)
                getDigits.addWait(length=1)
                getDigits.addSpeak("You have %d guesses remaining! Guess again!" % guesses)
                response.add(getDigits)
            else:
                response.addWait(length=1)
                response.addSpeak("Sorry, you don't have any remaining guesses. The secret was %d." % (secret))
                response.addHangup()
            return Response(str(response), mimetype='text/xml')


@app.route('/how_to_play', methods=['POST',])
def how_to_play():
    response = plivo.Response()
    response.addSpeak(body="I will think of a secret number that you will have to guess.")
    response.addSpeak(body="The number will be between one and one hundred.")
    response.addSpeak(body="To make your guess, just dial the digits and end with the hash sign.")
    response.addSpeak(body="For each wrong guess, I will tell you if you guessed lesser of greater.")
    response.addSpeak(body="You will have a maximum of ten chances to guess the number.")

    response.addWait(length=1)
    response.addSpeak(body="You will now be transferred to the main menu.")

    abs_red_url = url_for('index', _external=True)
    response.addRedirect(body=abs_red_url, method='POST')

    return Response(str(response), mimetype='text/xml')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
