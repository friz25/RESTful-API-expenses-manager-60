from flask import Flask, request, jsonify
app = Flask( __name__ )

@app.route('/login', methods=['GET', 'POST'])
def login():
    data = []
    if request.method == 'POST':
        data = [dict(id='1', name='max', email='max@gmail.com')]
        response = jsonify(data) # Converts your data strcuture into JSON format
        response.status_code = 202 #202 == "Accepted"

        return response
    else:
        data = [dict(id='none', name='none', email='none')]# Data structure of JSON format
        response = jsonify(data)
        response.status_code = 406 # 406 == "Not Acceptable"

        return response

@app.route('/')
def index():
    return 'Index page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/projects')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'