from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/Report', methods=['POST','GET'])
def Report():

    if request.method == 'POST' :
        username = request.form.get('username')
        email = request.form.get('email')
        print(username)
        print(email)

    return render_template('Report.html')
