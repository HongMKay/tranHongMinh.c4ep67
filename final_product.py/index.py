from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("homepage.html")

@app.route("/plants")
def plants():
    return render_template("plants.html")

@app.route("/animals")
def animals():
    return render_template("animals.html")

@app.route("/our_team")
def our_team():
    return render_template("our_team.html")

@app.route("/save_amazon")
def save_amazon():
    return render_template("save_amazon.html")
app.run(debug=True)