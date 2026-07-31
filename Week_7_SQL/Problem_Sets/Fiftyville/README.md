# Fiftyville

## What it does

Fiftyville is a SQL mystery investigation. Queries across crime reports, interviews, people, flights, phone calls, and financial records are used to identify the thief and the getaway destination.

## Use

Open the database and execute the investigation log:

```bash
sqlite3 fiftyville.db
sqlite> .read log.sql
```

The primary answers and query log are in this directory. A duplicate copy discovered nested inside the original Movies folder is preserved under `legacy_from_movies/`.
