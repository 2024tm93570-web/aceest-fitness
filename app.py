from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to ACEest Fitness & Gym"})

@app.route("/members")
def members():
    data = {
        "members": [
            {"name": "John", "membership": "Premium"},
            {"name": "Anna", "membership": "Basic"}
        ]
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)