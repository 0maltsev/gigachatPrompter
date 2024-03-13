import json
import logging
import os
import string

from flask import Flask, request, jsonify, make_response
import requests

app = Flask(__name__)

GIGACHAT_AUTHORIZATION: str = os.environ.get("GIGACHAT_AUTHORIZATION")
GIGACHAT_UID: str = os.environ.get("GIGACHAT_UID")
OPENAI_MODEL: str = os.environ.get("OPENAI_MODEL")

# create a test route
@app.route('/test', methods=['GET'])
def test():
    return make_response(jsonify({'message': 'test route'}), 200)


# get a product by id
def request_gigachat(prompt) -> str:
    return prompt


def generate_gigachat_token() -> str:
    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
    headers = {
        "Authorization": f"Basic {GIGACHAT_AUTHORIZATION}",
        "RqUID": f"{GIGACHAT_UID}",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    pr = {"scope": "GIGACHAT_API_CORP"}
    response = requests.post(url, headers=headers, data=pr).json()
    # TODO set as ENV VAR
    expires_at = response["expires_at"]

    return response["access_token"]


@app.route('/ask/', methods=['POST'])
def ask_gigachat():
    try:
        prompt = request.get_json()
        response = request_gigachat(prompt)
    except:
        return make_response(jsonify({'message': 'error asking gigachat'}), 404)
    return make_response(response)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.getenv("APP_PORT"))
