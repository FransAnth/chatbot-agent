import json
import os

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

from app.root_agent import ChatbotAgent

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "attachments/"


@app.route("/query-agent/", methods=["POST"])
@cross_origin(supports_credentials=True)
def query_agent():
    messages = json.loads(request.form.get("messages"))
    attachment = request.files.get("attachment")

    if attachment:
        filepath = os.path.join(UPLOAD_FOLDER, attachment.filename)
        attachment.save(filepath)
    else:
        filepath = None

    history_count_limit = 10
    prompt = construct_prompt(messages[history_count_limit * -1 :])

    chatbot = ChatbotAgent(image_path=filepath)
    response = chatbot.invoke(prompt)

    return jsonify(response)


def construct_prompt(messages):
    conversation = [
        f"{message.get('role')}: {message.get('content')}" for message in messages
    ]

    return "\n".join(conversation)


if __name__ == "__main__":
    app.run(debug=True)
