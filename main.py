from flask import Flask, request, jsonify
from flask_cors import CORS

from src.calendar import CalendarIO
from src.firestore import FirestoreIO

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:4200"}})


@app.route('/api/<collection>', methods=['POST'])
def insert(collection):
    firestore_io = FirestoreIO()
    firestore_io.insert(collection, request.get_json())
    return jsonify({})


@app.route('/api/<collection>/<id>', methods=['PATCH'])
def update(collection, id):
    firestore_io = FirestoreIO()
    firestore_io.update(collection, id, request.get_json())
    return jsonify({})


@app.route('/api/<collection>', methods=['GET'])
def get_all(collection):
    firestore_io = FirestoreIO()
    docs = firestore_io.list(collection)
    return jsonify(docs)


@app.route('/api/<collection>/<id>', methods=['DELETE'])
def delete(collection, id):
    firestore_io = FirestoreIO()
    firestore_io.delete(collection, id)
    return jsonify({})


@app.route('/api/users')
def list_users():
    firestore_io = FirestoreIO()
    users = firestore_io.list_users()
    return jsonify({'users': users})


@app.route('/api/calendar', methods=['POST'])
def create_calendar_event():
    calendar_io = CalendarIO()
    calendar_io.insert(request.get_json())
    return jsonify({})


if __name__ == '__main__':
    app.run()
