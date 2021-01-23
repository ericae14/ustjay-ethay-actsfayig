import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():
    response = requests.get("http://unkno.com")
    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


def piglatinize(phrase):
    session = requests.Session()
    response = session.post("https://hidden-journey-62459.herokuapp.com/piglatinize/", data = {'input_text': phrase}, allow_redirects=False)

    return response.headers["location"]


def get_result():
    phrase = get_fact()
    piglatin_phrase = piglatinize(phrase)

    return piglatin_phrase


@app.route('/')
def home():
    return get_result()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

