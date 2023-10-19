import datetime

from flask import Flask, request, render_template, url_for, redirect, abort, session

app = Flask(__name__)

app.secret_key = 'a4ca55aae18cfccfe1414c875b12bcf97f3df6f45d6cb81ea4b40964a588dcc2'

@app.route("/")
def hello_world():
    app.logger.info("this is an info msg")
    app.logger.error(f"this is an error msg {request.path}")
    return "<p>Hello, World! Andy</p>"


@app.route("/welcome/<name>")
def say_hi(name):
    active = False
    if 'username' in session:
        active = True
    return render_template('welcome.html', name=name, session_active=active)


@app.route("/years/<int:year>")
def say_years_old(year):
    today = datetime.date.today()
    current_year = today.year
    return f"<p>You are {current_year - year} years old</p>"


@app.route("/show/<name>", methods=['POST', 'GET'])
def show(name):
    return render_template('show.html', name=name)


@app.route("/redirect")
def do_redirect():
    return redirect(url_for('show', name='Joha'))


@app.route("/exit")
def do_exit():
    return abort(404)


@app.errorhandler(404)
def not_founf_page(error):
    return render_template('error404.html', error=error), 404  # this is a tupla

@app.route('/api/show/<name>', methods=['POST', 'GET'])
def show_json(name):
    return {'name': name, 'method_request' : request.method}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        app.logger.info('try login')
        username = request.form['username']
        session['username'] = username
        app.logger.debug(session)
        return redirect(url_for('say_hi', name=username))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('login'))

