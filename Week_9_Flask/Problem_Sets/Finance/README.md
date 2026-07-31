# Finance

## What it does

Finance is a Flask application for registering users, looking up stock quotes, buying and selling shares, and reviewing transaction history. It uses SQLite for persistence and Flask sessions for authentication state.

## Setup and run

Install the dependencies listed in `requirements.txt`:

```bash
python3 -m pip install -r requirements.txt
flask --app app run
```

Open the local Flask URL in a browser, register an account, and use the quote, buy, sell, and history routes. The source workspace included both the primary project database and a preserved snapshot under `data/finance_snapshot.db`.

The application expects the CS50 Finance helper environment and a working quote lookup configuration.
