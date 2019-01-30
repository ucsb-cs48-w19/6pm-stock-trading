from flask import Flask, render_template
from models import db, User

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


if __name__ == "__main__":
  app.run(debug=True)
