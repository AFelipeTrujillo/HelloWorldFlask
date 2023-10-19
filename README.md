## Basic commands

Simple route
```
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! Andy</p>"
```
How to run:
```
flask run
flask --debug run 
```

## Loggin
The object app has an atribute called logger
```
app.logger.info("this is a loggin msg")
```

## Template
* Create a folder named templates
* Create a html file called **show.html**
### Calling from app.py
```
@app.route("/show/<name>", methods=['POST', 'GET'])
def show(name):
    return render_template('show.html', name = name)
```
print var in html template:
```
<p>Your name is <strong>{{name}}</strong></p>
```

## Methods
This route recive POST and GET request
```
@app.route("/show/<name>", methods=['POST', 'GET'])
def show(name):
    return render_template('show.html', name = name)
```

## Redirect
### url_for
```
@app.route("/redirect")
def do_redirect():
    return redirect(url_for('show', name='Joha'))
```
Redirect in html template
```
<p><a href="{{url_for('hello_world')}}">Back to home</a></p>
    <p><a href="{{url_for('say_years_old', year=1988)}}">I am ?? years old</a></p>
```

## Error heandler
Use abort function
```
@app.route("/exit")
def do_exit():
    return abort(404)
```
User Error Handler decorator
```
@app.errorhandler(404)
def not_founf_page(error):
    return render_template('error404.html', error = error), 404 #thi is a tupla
```
## Apis
Just return a dictionary in python and flask converts automatically 
```
@app.route('/api/show/<name>', methods=['POST', 'GET'])
def show_json(name):
    return {'name': name, 'method_request' : request.method}
```

## Sessions
First you need create a session key with command
```
python -c 'import secrets; print(secrets.token_hex())'
```
Login & logout controller
```
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
```
Login form
```
<form method="POST" action="{{url_for('login')}}">
    <div>
        <label for="username">Username</label>
        <input type="text" name="username" >
    </div>
    <div>
        <label for="password">Password</label>
        <input type="password" name="password" >
    </div>
    <div>
        <button type="submit">Login</button>
    </div>
</form>
```


