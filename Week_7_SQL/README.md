# Week 7 — SQL

## Overview & Tech Stack

Week 7 introduces relational databases: tables, types, statements, constraints, indexes, functions, transactions, race conditions, and SQL injection. The focus shifts from controlling every loop to expressing a precise question over related data.

**Tech stack:** SQL, SQLite, relational schemas, joins, filtering, grouping, ordering, subqueries, and the `sqlite3` command-line client.

## Problem Sets Breakdown

- **Songs** — the numbered SQL files query a music database to identify artists, tracks, genres, durations, and popularity. The work relies on filtering, joins, ordering, and aggregate functions rather than a compiled program.
- **Movies** — the numbered queries explore relationships among films, ratings, people, directors, and release years. The key technique is joining normalized tables and narrowing the result with `WHERE`, `ORDER BY`, and nested queries.
- **Fiftyville** — `log.sql` records an investigation across crime reports, interviews, flights, phone calls, bank accounts, and bakery logs. The solution depends on progressively narrowing candidates through joins and subqueries; `answers.txt` records the final conclusion.

## Challenges & Reflections

SQL forced me to think in relationships instead of step-by-step loops. When a query returned too many rows, the problem was usually not the database—it was a missing join condition or an imprecise filter. Fiftyville was the first assignment where I had to keep a chain of evidence in my head across several tables, so I learned to write and verify one subquery at a time. The biggest improvement was learning to inspect the schema before guessing at column names.
