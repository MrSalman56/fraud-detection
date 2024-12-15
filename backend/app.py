from flask import Flask, request, jsonify
from flask_cors import CORS
import pymongo
import pandas as pd
from email_analyzer import analyze_email
from phishing_analyzer import analyze_link

app = Flask(__name__)
CORS(app)

# MongoDB Connection
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["fraud_detection_system"]
users_collection = db["users"]

# Routes
@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    users_collection.insert_one(data)
    return jsonify({"message": "User registered successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = users_collection.find_one({"email": data["email"], "password": data["password"]})
    if user:
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"message": "Invalid credentials"}), 401

@app.route('/email-fraud', methods=['POST'])
def email_fraud():
    data = request.json
    result = analyze_email(data['email_content'])  # Ensure 'email_content' is sent from frontend
    return jsonify(result), 200

@app.route('/phishing-detection', methods=['POST'])
def phishing_detection():
    data = request.json
    url = data.get('url')
    
    if not url:
        return jsonify({"result": "Error", "message": "No URL provided"}), 400
    
    print(f"Received URL: {url}")  # Debugging line
    
    # Call the phishing analysis function
    result = analyze_link(url)
    
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True)
