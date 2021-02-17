from flask import Flask, render_template


app = Flask(__name__)

# serve string
@app.route('/')
def index():
    msg = 'This is msg block.'
    return render_template('index.html', msg=msg)

# additional route with json
@app.route('/users')
def show_users():
    return {'users':['John Doe', 'Jane Doe']}

# route with variable
@app.route('/user/<username>')
def show_user(username):
    return {'user':username}

if __name__=='__main__':
    app.run(host='localhost', port=8080, debug=True)
