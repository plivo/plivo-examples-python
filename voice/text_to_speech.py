from flask import Flask, Response
from plivo import plivoxml

app = Flask(__name__)


@app.route("/speech/", methods=["GET", "POST"])
def speak_xml():

    # Generate a Speak XML with the details of the text to play on the call.
    response = (
        plivoxml.ResponseElement()
        .add(plivoxml.SpeakElement("This is English!", voice="MAN", language="en-GB"))
        .add(
            plivoxml.SpeakElement(
                "Ce texte généré aléatoirement peut-être utilisé dans vos maquettes",
                voice="MAN",
                language="fr-FR",
            )
        )
        .add(
            plivoxml.SpeakElement(
                "Это случайно сгенерированный текст может быть использован в макете",
                voice="MAN",
                language="ru-RU",
            )
        )
    )
    return Response(response.to_string(), mimetype="application/xml")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)


# Sample successful output
# <Response>
#   <Speak voice="MAN" language="en-GB">This is English!</Speak>
#   <Speak voice="MAN" language="fr-FR">Ce texte généré aléatoirement peut-être utilisé dans vos maquettes</Speak>
#   <Speak voice="MAN" language="ru-RU">Это случайно сгенерированный текст может быть использован в макете</Speak>
# </Response>