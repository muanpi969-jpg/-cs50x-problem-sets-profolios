import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")

        if name and month and day:
            con = sqlite3.connect("birthdays.db")
            db = con.cursor()

            db.execute(
                "INSERT INTO birthdays (name, month, day) VALUES (?, ?, ?)",
                (name, month, day)
            )

            con.commit()
            con.close()

        return redirect("/")

    else:
        con = sqlite3.connect("birthdays.db")
        db = con.cursor()

        db.execute("SELECT name, month, day FROM birthdays")
        birthdays = db.fetchall()

        con.close()

        return render_template("index.html", birthdays=birthdays)
