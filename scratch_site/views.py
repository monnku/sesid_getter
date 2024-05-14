from testapp import app
import request

@app.route('/datas', methods=['POST'])
def sample_form_temp():
    user = request.form['username']
    pw = request.form['password']
    return f'user:{user}'
