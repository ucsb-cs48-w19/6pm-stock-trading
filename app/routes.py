from flask import Flask, render_template, request, session, redirect, url_for
from models import db, User
from forms import SignupForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:trader@localhost/db'
db.init_app(app)

app.secret_key = "development-key"

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/dashboard")
def dashboard():
  return render_template("dashboard.html")

@app.route("/personal-info")
def personal_info():
  return render_template("personal-info.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/login", methods = ['GET', 'POST'])
def authenticate_user():
	print("Login Processing ")
	return render_template("index.html")

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
      return redirect(url_for('dashboard'))

  elif request.method == "GET":
    return render_template('signup.html', form=form)

@app.route("/logout")
def logout():
  session.pop('email', None)
  return redirect(url_for('index'))


if __name__ == "__main__":
  app.run(debug=True)
