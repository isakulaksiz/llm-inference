from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Modeli yükle
generator = pipeline("text-generation", model="gpt2")

@app.route("/generate", methods=["POST"])
def generate_text():
    data = request.get_json()
    prompt = data.get("prompt", "")
    max_length = data.get("max_length", 50)

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    result = generator(prompt, max_length=max_length)
    return jsonify({"generated_text": result[0]["generated_text"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5054)
