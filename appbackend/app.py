from flask import Flask, request, jsonify, session, redirect, url_for
from flask_session import Session
import json
from flask_cors import CORS
from functools import wraps

app = Flask(__name__)
CORS(app)

# Secret key for session signing (change it in production)
app.secret_key = 'your_secret_key'
app.config['SESSION_TYPE'] = 'filesystem'  # Use filesystem to store session data
Session(app)

user_json = open('static/users.json', 'r')
users = json.loads(user_json.read())

