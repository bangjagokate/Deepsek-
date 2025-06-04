from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/api/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message", "")
    api_key = os.environ.get("sk-c72130f0387944fb9b50fa0cedd12dbe")  # API key dari environment
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ],
        "stream": False
    }

    res = requests.post("https://api.deepseek.com/chat/completions", headers=headers, json=payload)
    data = res.json()
    
    try:
        reply = data['choices'][0]['message']['content']
        return jsonify({"reply": reply})
    except:
        return jsonify({"reply": "Gagal mendapatkan respons.", "error": data})

@app.route('/')
def home():
    return "API DeepSeek aktif."

if __name__ == '__main__':
    app.run()
