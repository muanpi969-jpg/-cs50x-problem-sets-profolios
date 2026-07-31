from flask import Flask, render_template, request, redirect
from cs50 import SQL

app = Flask(__name__)

db = SQL("sqlite:///habits.db")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        habit = request.form.get("habit")
        if habit:
            db.execute("INSERT INTO habits (name) VALUES (?)", habit)
        return redirect("/")

    habits = db.execute("SELECT * FROM habits")
    return render_template("index.html", habits=habits)
