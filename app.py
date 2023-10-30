from flask import Flask, jsonify, render_template, request, redirect, url_for 
from flask_cors import CORS
import psycopg2

app=Flask(__name__)
CORS(app)

try:
    conn = psycopg2.connect(
        host='csce-315-db.engr.tamu.edu',
        database='csce315_902_01db',
        user='csce315_902_01user',
        password='1234'
    )
    print('Connection success')
except psycopg2.Error as e:
    print("Connection error:", e)

@app.route('/')
def index():
    return '<h1>Default Page</h1> <h3>Hello World from Flask</h3>'

@app.route('/two')
def two():
    return '<h1>Default Page</h1> <h1>Man Reference</h1>'

@app.route('/currentMenu')
def currentMenu():
    cur = conn.cursor()
    query = 'SELECT * FROM menu'

    cur.execute(query)
    result = cur.fetchall()

    answer = {}
    for i, row in enumerate(result):
        currMap = {}
        currItem = row[0]
        currMap['price'] = row[1]
        currMap['ingredients'] = row[2]

        answer[currItem] = currMap

    return jsonify(answer)

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8000)