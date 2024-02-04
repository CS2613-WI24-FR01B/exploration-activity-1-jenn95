# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request, session, flash
from twilio.rest import Client
from functools import wraps

app = Flask(__name__)

account_sid = "AC15d3034aa47604f06b5b17f9199c2f75"
auth_token  = "24448c148db63e40ce5a382d9764ff65"

client = Client(account_sid, auth_token)

#could be random
app.secret_key = "shh"

#decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Your must be logged in to access this content')
            return redirect(url_for('login'))    


@app.route('/')
def home():
    return render_template('welcome.html')   


@login_required
@app.route('/subscribe', endpoint='subscribe', methods=['GET', 'POST'])
def subscribe():
    error = None
    if request.method == 'POST':
        if len(request.form['number']) < 11:
            error = 'Invalid Number. Please try again with format: +15061234567'
        else:
            try:
                client.messages.create(to=request.form['number'],from_="+14423337508",body="Thanks for subscribing to the demo!")
                flash('Thanks, '+ request.form['name']+'! You were added to the subscription list.')
            except:
                error = 'Invalid number. This number has not been configured with the *Trial* Twilio Account'
    return render_template('subscribe.html', error=error)      


remainingDates = ["Jan-23", "Jan-23" ,"Jan-30", "Feb-6", "Feb-13", "Feb-20", "Feb-27", "Mar-12", "Mar-19", "Mar-26", "Apr-02", "Apr-09"]
completedPQs=[]
@app.route('/todo', endpoint='todo', methods=['GET', 'POST'])
def todo():
    error = None
    if request.method == 'POST':
        flash('You just completed PQ '+ request.form['language']+ request.form['number'])
        if request.form['date'] in remainingDates:
            remainingDates.remove(request.form['date']);
        question = [request.form['date'], request.form['language'],request.form['number']]
        completedPQs.append(question)
        flash('You have completed ' + str(len(completedPQs)) + ' and have ' + str(len(remainingDates)) + ' remaining.')
        return redirect(url_for('todo'))
    return render_template('todo.html', error=error, remainingDates=remainingDates, completedPQs=completedPQs)      


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'

        else:
            session['logged_in'] = True
            return redirect(url_for('restrictedAdmin'))
    return render_template('login.html', error=error)

@login_required
@app.route ('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were just logged out')
    return redirect(url_for('home'))


@login_required
@app.route('/restrictedAdmin')
def restrictedAdmin():
    subscriber_list = []
    for sms in client.messages.list():
        subscriber_list.append(sms.to)
    return render_template('restrictedAdmin.html', subList=subscriber_list)   

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(port=8082, debug=True)
