import os
from datetime import datetime
import time
from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user, LoginManager, login_required
from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, FloatField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from werkzeug.urls import url_parse
#Added imports for postgres hsoting
from flask_sqlalchemy import SQLAlchemy
from graph import graphMaker

app = Flask(__name__)

#Added initializations for postgres hosting
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'signin'
@login.user_loader
def user_loader(id):
  return User.query.get(id)
from models import *





#from forms import SignupForm








class SignupForm(Form):
  first_name = StringField('First name', validators=[DataRequired("Please enter your first name.")])
  last_name = StringField('Last name', validators=[DataRequired("Please enter your last name.")])
  email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter your email address.")])
  password = PasswordField('Password', validators=[DataRequired("Please enter a password."), Length(min=6, message="Passwords must be 6 characters or more.")])


  initial_investment = FloatField('Initial Investment')
  
  submit = SubmitField("Sign Up")


  def validate_email(self, email):
    user = User.query.filter_by(email=email.data).first()
    if user is not None:
      raise ValidationError('Please use a different email address')




class LoginForm(Form):
  email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter your email address.")])
  password = PasswordField('Password', validators=[DataRequired("Please enter a password.")])
  remember_me = BooleanField('Remember Me')
  submit = SubmitField("Sign in")


class PersonalInfo(Form):
  initial_investment = FloatField('Initial Investment', validators=[DataRequired("Please enter an amount. ")])
  risk = BooleanField('Risk')

  submit = SubmitField("Save")



#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:trader@localhost/db'
#db.init_app(app)

app.secret_key = "development-key"


@app.route("/")
def index():
  graphUrl = graphMaker()
  return render_template("index.html", graphUrl=graphUrl)


@app.route("/about")
def about():
  return render_template("about.html")


@app.route("/dashboard")
@login_required
def dashboard():
  print('in dashboard')
  user = current_user
  #user = User.query.filter_by(email=session['email']).first()
  if user is not None:
    initial_investment = user.initial_investment
    balance = user.balance
    change = balance-initial_investment
    print('numbers')
    print(initial_investment, balance, change)
    return render_template("dashboard.html", initial_investment=round(initial_investment, 2), balance=round(balance, 2), change=round(change, 2), risk=user.risk)
  else:
    return redirect(url_for('index'))
#return render_template("dashboard.html")


@app.route("/personal-info",  methods=["GET", "POST"])
def personal_info():
  form = PersonalInfo()
  if request.method == "POST":
    if form.validate() == False:
      return render_template('personal-info.html', form=form)
    else:
      current_user.initial_investment = form.initial_investment.data
      current_user.balance = form.initial_investment.data
      current_user.risk = form.risk.data
      print ('!!!!!!! ', form.risk.data)
      db.session.commit()
      return redirect(url_for('dashboard'))

  elif request.method == "GET":
    return render_template('personal-info.html', form=form)



@app.route("/login", methods=["GET", "POST"])
def signin():
  if current_user.is_authenticated:
    return redirect(url_for('index'))

  form = LoginForm()
  if form.validate_on_submit():
    email = form.email.data
    password = form.password.data
    user = User.query.filter_by(email=email).first()
    if user is None or not user.check_password(form.password.data):
      flash('Invalid username or password')
      return redirect(url_for('signin'))
    login_user(user, remember=form.remember_me.data)
    flash('Welcome back, ' + current_user.firstname)
    return redirect(url_for('dashboard'))

  return render_template('login.html', form=form)


'''
  if request.method == "POST":
    if form.validate() == False:
      return render_template("login.html", form=form)
    else:
      email = form.email.data
      password = form.password.data
      #print(email, '\n', password)

      user = User.query.filter_by(email=email).first()
      #print(user, '\n', user.check_password(password))
      if user is not None and user.check_password(password):
    
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
          next_page = url_for('index')
        return redirect(next_page)
      else:
        flash('Invalid Username or Password')
        return redirect(url_for('login'))

  elif request.method == 'GET':'''
    

@app.route("/signup", methods=["GET", "POST"])
def signup():
  if current_user.is_authenticated:
    return redirect(url_for('dashboard'))

  form = SignupForm()

  if request.method == "POST":
    if form.validate() == False:
      return render_template('signup.html', form=form)
    else:
      newuser = User(form.first_name.data, form.last_name.data, form.email.data, form.password.data)
      db.session.add(newuser)
      db.session.commit()
      login_user(newuser)
      flash("Account created successfully!")
      return redirect(url_for('personal_info'))

  elif request.method == "GET":
    return render_template('signup.html', form=form)

@app.route("/withdraw_funds")
@login_required
def profile():
  return render_template("withdraw-funds.html")

@app.route("/goodbye")
@login_required
def goodbye():
  db.session.delete(current_user)
  db.session.commit()
  logout_user()
  flash('Funds transferred and account closed successfully!')
  return render_template("goodbye.html")


@app.route("/logout")
@login_required
def logout():
  name = current_user.firstname
  logout_user()
  flash('Successfully logged out')
  return redirect(url_for('index'))


if __name__ == "__main__":
  app.run(debug=True)
