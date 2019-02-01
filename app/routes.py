from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/dashboard")
def dashboard():
  return render_template("dashboard.html")
@app.route("/login")
def login():
    return render_template("login.html")
    
@app.route("/login", methods = ['GET', 'POST'])
def authenticate_user():
	print("Login Processing ") 
	return render_template("index.html")

	#process user data from the post request




if __name__ == "__main__":
  app.run(debug=True)
