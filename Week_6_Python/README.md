# Week 6 — Python

## Overview & Tech Stack

Week 6 revisits functions, arguments, return values, variables, Boolean expressions, conditionals, and loops in Python, then adds modules, packages, dictionaries, lists, strings, and higher-level file handling.

**Tech stack:** Python 3, standard-library string and file operations, dictionaries and lists, command-line arguments, and CSV/text data.

## Problem Sets Breakdown

- **Hello** — `hello.py` reads a name and formats a greeting, showing Python's concise input and string handling.
- **Mario** — `mario.py` validates the height and builds the pyramid with nested loops, carrying the same algorithm from C into Python's syntax.
- **Cash** — `cash.py` calculates the fewest coins needed for change using Python's numeric operations and control flow.
- **Readability** — `readability.py` counts letters, words, and sentences, then applies the Coleman–Liau formula to classify a passage.
- **DNA** — `dna.py` reads an STR database and sequence file, computes the longest consecutive run for each STR, and compares the resulting profile against each database row.

## Challenges & Reflections

Transitioning to Python's dynamic typing felt strange after weeks of strict C types. I initially missed compiler feedback, especially when a value had the wrong shape but was still accepted by the interpreter. At the same time, dictionaries and string operations made DNA much easier to express than it would have been in C. Reimplementing Mario and Readability helped me separate the algorithm from the language: the reasoning stayed the same even when the syntax and error model changed.
