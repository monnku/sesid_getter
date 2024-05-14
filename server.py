from testapp import app
from flask import render_template, request

@app.route('/', methods=['GET'])
def form():
    return render_template('index.html')

@app.route('/sesid_getter/data', methods=['POST'])
def do():
    user = request.form['username']
    pw = request.form['password']
    return render_template('index.html')
