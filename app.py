from flask import Flask, jsonify, render_template, request, redirect, url_for 
from flask_cors import CORS
import psycopg2

app=Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return '<h1>Default Page</h1> <h3>Hello World from Flask</h3>'

@app.route('/two')
def two():
    return '<h1>Default Page</h1> <h1>Man Reference</h1>'