# Version 2.0.0 - Kubernetes ready
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to ACEest Fitness & Gym",
        "version": "2.0.0"
    })

@app.route("/members")
def members():
    data = {
        "members": [
            {"name": "John", "membership": "Premium"},
            {"name": "Anna", "membership": "Basic"},
            {"name": "Ravi", "membership": "Premium"}
        ]
    }
    return jsonify(data)

@app.route("/classes")
def classes():
    data = {
        "classes": [
            {"name": "Yoga", "time": "6:00 AM"},
            {"name": "Zumba", "time": "8:00 AM"},
            {"name": "CrossFit", "time": "7:00 PM"}
        ]
    }
    return jsonify(data)

@app.route("/health")
def health():
    return jsonify({"status": "healthy", "version": "2.0.0"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)