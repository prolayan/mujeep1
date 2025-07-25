from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.environ['OPENAI_API_KEY']

# ✅ هذا الـ GET عشان المتصفح يختبر الرابط
@app.route('/', methods=['GET'])
def home():
    return "Mujeeb API is running ✅"

# ✅ هذا هو اللي يستخدمه React و Hoppscotch
@app.route('/', methods=['POST'])
def mujeeb():
    data = request.json
    message = data.get("message", "")

    if not message:
        return jsonify({"reply": "لم أفهم، حاول مرة أخرى."}), 400

    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "أنت مساعد بنكي صوتي للمكفوفين، اسمه مجيب. كن واضحًا وبسيطًا."},
            {"role": "user", "content": message},
        ]
    )

    reply = completion['choices'][0]['message']['content']
    return jsonify({"reply": reply})


# ✅ ضروري لتشغيل السيرفر في Render
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
