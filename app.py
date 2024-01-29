from flask import Flask, render_template, request
import database

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('register_user.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        credentials = database.varify(username, password)
        if credentials: message = 'Username {0}. is logged in'.format(username)
        else: message = 'Error Occured.'
        return render_template('status_register.html', message=message)
    
    return render_template('login_user.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    
    status = database.store(username, password)

    if status: message = 'User {0} is successfully created.'.format(username)
    else: message = 'Error Occured.'

    return render_template('status_user_creation.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)
