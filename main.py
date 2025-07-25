
from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)
client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

@app.route('/', methods=['POST'])
def mujeeb():
    data = request.json
    message = data.get("message", "")

    if not message:
        return jsonify({"reply": "لم أفهم، حاول مرة أخرى."}), 400

    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "أنت مساعد بنكي صوتي للمكفوفين، اسمه مجيب. كن واضحًا وبسيطًا."},
            {"role": "user", "content": message},
        ]
    )

    reply = completion.choices[0].message.content
    return jsonify({"reply": reply})
