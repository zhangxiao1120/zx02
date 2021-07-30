from flask import Flask, redirect, url_for,render_template,request,flash
app = Flask(__name__)
app.secret_key = 'random string'

@app.route('/admin')
def hello_admin():
   return 'Hello World s!'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
   if name == 'a':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest', guest=name))

@app.route("/")
def index():
   return render_template("test.html")

@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
            request.form['password'] != 'admin':
            error = 'Invalid username or password. Please try again!'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))

    return render_template('login.html', error = error)

if __name__ == '__main__':
   app.run(debug=True)