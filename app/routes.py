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

@app.route("/personal-info")
def personal_info():
	return render_template("personal-info.html")




if __name__ == "__main__":
	app.run(debug=True)
