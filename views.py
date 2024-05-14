from testapp import app
from flask import render_template, request

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        user = request.form['username']
        pw = request.form['password']
        return 'test'
