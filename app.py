from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "")
    # Replace with actual AI logic later
    return jsonify({"answer": f"You said: {question[::-1]}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
