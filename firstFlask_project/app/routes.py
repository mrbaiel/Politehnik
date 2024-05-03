from app import app
from flask import render_template


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/schedule")
def schedule():
    return render_template("schedule.html")

@app.route("/coaches")
def coaches():
    return render_template("coaches.html")