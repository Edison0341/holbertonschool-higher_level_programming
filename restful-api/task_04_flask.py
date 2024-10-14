#!/usr/bin/python3
from flask import Flask, jsonify, request


app = Flask(__name__)

users_data = {
    "jane": {
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    }
}


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/data')
def data():
    return (jsonify(users_data))


@app.route('/status')
def status():
    return ("OK")


@app.route('/users/<username>')
def get_user(username):
    user = users_data.get(username)
    if user:
        return (jsonify(user))
    else:
        return (jsonify({"error": "User not foung"}), 404)


@app.route('/add_user', methods=['POST'])
def add_user():
    new_user = request.get_json()
    required_keys = ['username', 'name', 'age', 'city']
    if not new_user or not all(key in new_user for key in required_keys):
        return (jsonify({"error":
                "Invalid data. Username, name, age, and city are required."}),
                400)

    username = new_user['username']

    if username in users_data:
        return (jsonify({"error": "User already exits"}), 400)

    users_data[username] = {
        "name": new_user['name'],
        "age": new_user['age'],
        "city": new_user['city']
    }

    return (jsonify({"message": "User added succesfully.",
                    "user": users_data[username]}), 201)


if __name__ == '__main__':
    app.run(debug=True)
