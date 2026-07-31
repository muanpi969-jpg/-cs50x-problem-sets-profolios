import os
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

app = Flask(__name__)

app.jinja_env.filters["usd"] = usd

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///finance/project/habits.db")


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# ================= INDEX =================
@app.route("/")
@login_required
def index():
    user_id = session["user_id"]

    stocks = db.execute("""
        SELECT symbol, SUM(shares) as shares
        FROM transactions
        WHERE user_id = ?
        GROUP BY symbol
        HAVING shares > 0
    """, user_id)

    total = 0

    for stock in stocks:
        quote = lookup(stock["symbol"])
        stock["price"] = quote["price"]
        stock["total"] = stock["shares"] * stock["price"]
        total += stock["total"]

    cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
    grand_total = total + cash

    return render_template("index.html", stocks=stocks, cash=cash, grand_total=grand_total)


# ================= REGISTER =================
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Validate username
        if not username:
            return apology("must provide username")

        # Validate password
        if not password:
            return apology("must provide password")

        # Validate confirmation
        if password != confirmation:
            return apology("passwords must match")

        # Insert user
        try:
            user_id = db.execute(
                "INSERT INTO users (username, hash) VALUES (?, ?)",
                username,
                generate_password_hash(password)
            )
        except:
            return apology("username already exists")

        # Log user in automatically
        session["user_id"] = user_id

        # Redirect to portfolio
        return redirect("/")

    else:
        return render_template("register.html")


# ================= LOGIN =================
@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()

    if request.method == "POST":

        if not request.form.get("username"):
            return apology("must provide username", 403)

        if not request.form.get("password"):
            return apology("must provide password", 403)

        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        session["user_id"] = rows[0]["id"]
        return redirect("/")

    else:
        return render_template("login.html")


# ================= LOGOUT =================
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


# ================= QUOTE =================
@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():

    if request.method == "POST":

        symbol = request.form.get("symbol")

        if not symbol:
            return apology("must provide symbol")

        stock = lookup(symbol)

        if stock is None:
            return apology("invalid symbol")

        return render_template("quoted.html", stock=stock)

    else:
        return render_template("quote.html")


# ================= BUY =================
@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():

    if request.method == "POST":

        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        if not symbol:
            return apology("must provide symbol")

        stock = lookup(symbol)
        if stock is None:
            return apology("invalid symbol")

        if not shares.isdigit() or int(shares) <= 0:
            return apology("invalid shares")

        shares = int(shares)
        price = stock["price"]
        total_cost = price * shares

        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]

        if cash < total_cost:
            return apology("can't afford")

        db.execute("UPDATE users SET cash = cash - ? WHERE id = ?", total_cost, session["user_id"])

        db.execute("""
            INSERT INTO transactions (user_id, symbol, shares, price, type)
            VALUES (?, ?, ?, ?, 'BUY')
        """, session["user_id"], symbol.upper(), shares, price)

        return redirect("/")

    else:
        return render_template("buy.html")


# ================= SELL =================
@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():

    if request.method == "POST":

        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        if not shares.isdigit() or int(shares) <= 0:
            return apology("invalid shares")

        shares = int(shares)

        owned = db.execute("""
            SELECT SUM(shares) as total
            FROM transactions
            WHERE user_id = ? AND symbol = ?
        """, session["user_id"], symbol)[0]["total"]

        if owned is None or owned < shares:
            return apology("not enough shares")

        stock = lookup(symbol)
        price = stock["price"]
        total = shares * price

        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", total, session["user_id"])

        db.execute("""
            INSERT INTO transactions (user_id, symbol, shares, price, type)
            VALUES (?, ?, ?, ?, 'SELL')
        """, session["user_id"], symbol, -shares, price)

        return redirect("/")

    else:
        symbols = db.execute("""
            SELECT symbol FROM transactions
            WHERE user_id = ?
            GROUP BY symbol
            HAVING SUM(shares) > 0
        """, session["user_id"])

        return render_template("sell.html", symbols=symbols)


# ================= HISTORY =================
@app.route("/history")
@login_required
def history():

    history = db.execute("""
        SELECT symbol, shares, price, type, time
        FROM transactions
        WHERE user_id = ?
        ORDER BY time DESC
    """, session["user_id"])

    return render_template("history.html", history=history)
