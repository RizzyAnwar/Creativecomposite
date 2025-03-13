from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    topic = data.get("topic", "default topic")
    response = f"Generated AI content for: {topic}"  # Placeholder for OpenAI integration
    return jsonify({"result": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
