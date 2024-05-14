from testapp import app
import request

@app.route('/sesid_getter', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        user = request.form['username']
        pw = request.form['password']
        return 'test'
