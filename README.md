# CS50x Portfolio

[![C](https://img.shields.io/badge/C-00599C?logo=c&logoColor=white)](https://en.cppreference.com/w/c)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![SQL](https://img.shields.io/badge/SQL-4479A1?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![HTML/CSS](https://img.shields.io/badge/HTML%2FCSS-E34F26?logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Learn)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Flask](https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)

## About

This repository is my working portfolio for **CS50x: Introduction to Computer Science** from Harvard University. It documents the progression from computational thinking and C fundamentals through algorithms, memory, data structures, Python, SQL, web programming, Flask, artificial intelligence, and a final project.

The folders contain personal lecture practice, problem-set implementations, SQL investigations, web exercises, supporting data, and Flask applications. The code is intentionally preserved as coursework snapshots so the repository shows both the solutions and the learning progression behind them.

## Contents

- [Week 0 — Scratch](./Week_0_Scratch/)
- [Week 1 — C](./Week_1_C/)
- [Week 2 — Arrays](./Week_2_Arrays/)
- [Week 3 — Algorithms](./Week_3_Algorithms/)
- [Week 4 — Memory](./Week_4_Memory/)
- [Week 5 — Data Structures](./Week_5_Data_Structures/)
- [Week 6 — Python](./Week_6_Python/)
- [Week 7 — SQL](./Week_7_SQL/)
- [Artificial Intelligence](./Artificial_Intelligence/)
- [Week 8 — HTML, CSS, JavaScript](./Week_8_HTML_CSS_JavaScript/)
- [Week 9 — Flask](./Week_9_Flask/)
- [Week 10 — The End](./Week_10_The_End/)
- [Final Project](./Final_Project/)

## How to run the coursework

Most programs are designed for a CS50 Codespace or another environment with the CS50 libraries installed. Run each program from its own folder so relative paths to databases, templates, dictionaries, and sample data remain correct.

### C

For a simple C program using the CS50 library:

```bash
clang mario.c -o mario -lcs50
./mario
```

Assignments with a `Makefile` can be built with `make`, for example:

```bash
cd Week_4_Memory/Problem_Sets/Filter
make filter
./filter -g input.bmp output.bmp
```

### Python

Run a Python exercise with:

```bash
python3 program.py
```

For programs that accept command-line arguments, follow the usage string printed by the program. The DNA exercise, for example, expects a database file and a sequence file.

### SQL

Use SQLite to inspect a database and run a query file:

```bash
cd Week_7_SQL/Problem_Sets/Songs
sqlite3 songs.db
sqlite> .read 1.sql
```

### HTML, CSS, and JavaScript

Open a page directly in a browser or serve its directory locally:

```bash
python3 -m http.server 8000
```

Then visit `http://localhost:8000/`.

### Flask

Install the dependencies listed by the application, then start Flask from the project directory:

```bash
python3 -m pip install -r requirements.txt
flask --app app run
```

Some coursework snapshots are incomplete or retain the original course environment's assumptions, so the week-level README should be treated as the authoritative run guide for each project.

## Academic honesty

These are my personal solutions and learning notes. Current CS50 students should follow [CS50's academic honesty policy](https://cs50.harvard.edu/x/honesty/) and should not use this repository to bypass the course's learning process or submit copied work.

## Let's connect

- LinkedIn: `https://www.linkedin.com/in/your-profile/`
- Portfolio: `https://your-portfolio.example.com/`
- GitHub: `https://github.com/your-username/`
