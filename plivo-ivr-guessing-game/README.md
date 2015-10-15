Plivo Guessing Game
===================

An IVRS based <b>Guess the Number Game<b> using the Plivo Platform.

The game is an IVRS application that can be attached to a Plivo DID or
used as a SIP endpoint. When the application is called, the voice asks
you to guess a secret number between 1 and 100 over multiple turns by
pressing digits on your phone in each turn.

Once you run out of turns or you correctly guess the secret number,
the voice tells you your score for this round of the game and hangs
up.

The application is hosted on Heroku at
<http://plivo-guessing-game.herokuapp.com/> and can be readily used by
specifying this URL as the answer URL in your Plivo account.

The `plivo-ivr-guessing-game` folder can be deployed on Heroku easily.

Technical Notes
---------------

This section requires an understanding of the GetDigits XML element as
implemented by Plivo. To refresh your memory head over to the
documentation at <https://plivo.com/docs/xml/getdigits/>.

The application picks a random number between 1 and 100 for the
secret. This secret number and the number of turns remaining is sent
to the Plivo Platform as a GET parameter in the Action URL in the
GetDigits element. When the user presses a digit the action URL
receives the digit, and the GET parameters to check the guess and make
an appropriate response.
