from testapp import app
import request

@app.route('/')
def index():
    return '<!DOCTYPE html><head><meta charset="utf-8"><title>scratch sid_returner</title></head><body><h2>username:</h2><input class="username"><br><h2>password</h2><input class="password"><button class="btn">submit</button></body>'

@app.route('/datas', methods=['POST'])
def sample_form_temp():
    req1 = request.form['username']
    req2 = request.form['password']
    return req1
