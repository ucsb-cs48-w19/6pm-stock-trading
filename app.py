import os
from flask import Flask, render_template, request, session, redirect, url_for
from forms import SignupForm, LoginForm, InitialInvestmentForm

#Added imports for postgres hsoting
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#Added initializations for postgres hosting
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
from forms import SignupForm
from models import *



#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:trader@localhost/db'
#db.init_app(app)

app.secret_key = "development-key"


@app.route("/")
def index():
  return render_template("index.html")


@app.route("/about")
def about():
  return render_template("about.html")


@app.route("/dashboard")
def dashboard(): 
  user = User.query.filter_by(email=email).first()
  if user is not None and user.check_password(password):
    initial_investment = session["initial_investment"]
    balance = session["balance"]
    change = balance-initial_investment
    return render_template("dashboard.html", initial_investment=initial_investment, balance=balance, change=change)
  return render_template("dashboard.html")


@app.route("/personal-info", methods=["GET", "POST"])
def personal_info():
  return render_template("personal-info.html")

  risk0 = request.form['risk0']
  risk1 = request.form['risk1']
  initial_investment = request.form['capital']


  form = C()


@app.route("/login", methods=["GET", "POST"])
def login():
  if 'email' in session:
    return redirect(url_for('dashboard'))

  form = LoginForm()

  if request.method == "POST":
    if form.validate() == False:
      return render_template("login.html", form=form)
    else:
      email = form.email.data
      password = form.password.data

      user = User.query.filter_by(email=email).first()
      if user is not None and user.check_password(password):
        session['email'] = form.email.data
        return redirect(url_for('dashboard'))
      else:
        return redirect(url_for('login'))

  elif request.method == 'GET':
    return render_template('login.html', form=form)

@app.route("/signup", methods=["GET", "POST"])
def signup():
  if 'email' in session:
    return redirect(url_for('dashboard'))

  form = SignupForm()

  if request.method == "POST":
    if form.validate() == False:
      return render_template('signup.html', form=form)
    else:
      newuser = User(form.first_name.data, form.last_name.data, form.email.data, form.password.data)
      db.session.add(newuser)
      db.session.commit()

      session['email'] = newuser.email
      return redirect(url_for('personal-info.html'))

  elif request.method == "GET":
    return render_template('signup.html', form=form)


@app.route("/logout")
def logout():
  session.pop('email', None)
  return redirect(url_for('index'))


if __name__ == "__main__":
  app.run(debug=True)
