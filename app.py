from flask import Flask, jsonify, request
from flask_cors import CORS 
app = Flask(__name__)
CORS(app)
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]


@app.route('/', methods=['GET'])
def get_users():
    return jsonify(users)


@app.route('/', methods=['POST'])
def post_users():
    data = request.get_json()  
    return jsonify(data), 200 

if __name__ == '__main__':
    app.run(debug=True)
