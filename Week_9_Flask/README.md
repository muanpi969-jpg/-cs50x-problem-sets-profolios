# Week 9 — Flask

## Overview & Tech Stack

Week 9 connects Python to the web through Flask routes, decorators, requests, responses, templates, sessions, cookies, and database-backed applications.

**Tech stack:** Python 3, Flask, Jinja templates, SQLite, the CS50 SQL helper, Flask-Session, Werkzeug password hashing, HTTP forms, and CSS.

## Problem Sets Breakdown

- **Birthdays** — `app.py` handles GET and POST requests, validates a name/month/day form, inserts records with parameterized SQL, queries saved birthdays, and passes them to a template. The current HTML snapshot is misaligned with that backend and still contains a registration form, so the project is best understood as an incomplete coursework state.
- **Finance** — `app.py` implements registration, login, logout, quote lookup, buying, selling, and portfolio calculations. `helpers.py` provides authentication guards, quote requests, error rendering, and currency formatting. Templates represent the application shell and its transaction forms. The current snapshot still points at an old database path and does not include a complete index template, so it requires environment cleanup before it is turnkey.

## Challenges & Reflections

Flask was where isolated functions finally had to cooperate across requests. I had to reason about what belonged in the URL, the form body, the session, the database, and the template context. A page could fail even when the route was correct if the template expected a different variable name. That made me appreciate the value of tracing one request end to end, and it also taught me to document incomplete wiring instead of pretending a coursework snapshot is production-ready.
