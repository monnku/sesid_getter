from testapp import app
import request

@app.route('/datas', methods=['POST'])
def sample_form_temp():
    req1 = request.form['username']
    req2 = request.form['password']
    return req1
