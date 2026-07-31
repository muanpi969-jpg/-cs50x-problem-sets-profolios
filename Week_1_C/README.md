# Week 1 — C

## Overview & Tech Stack

Week 1 introduces compilation, source code, machine code, libraries, types, variables, conditionals, loops, comments, command-line work, integer overflow, and floating-point imprecision.

**Tech stack:** C, the CS50 library (`get_int`, `get_char`, `get_long`, and `get_string`), `clang`, `make`, and the command line.

## Problem Sets Breakdown

- **Hello** — `helloname.c` reads a name with `get_string` and prints a formatted greeting. It is a small exercise in input, strings, and standard output.
- **Mario** — `mario.c` validates a positive height with a `do ... while` loop, then uses nested loops to print leading spaces and hash characters for each row of a pyramid.
- **Credit** — `credit.c` applies Luhn's checksum from right to left, then counts digits and inspects the leading digits to classify American Express, MasterCard, Visa, or an invalid number.
- **Lecture practice** — `hello.c`, `meow.c`, `agree.c`, `compare.c`, `calculator.c`, `calculator2.c`, and `buggy.c` cover greeting output, repetition, Boolean conditions, arithmetic branches, unbounded loops, and debugging a malformed increment expression.

## Challenges & Reflections

I spent more time than expected understanding why C input and output needed explicit types. A string is not just a convenient value, and an integer division can silently discard information. The Credit exercise was the first place where a short program required several passes over the same data, so I had to be deliberate about whether I was reading the original number or a temporary copy. Debugging `buggy.c` also made the compiler feel less like an obstacle and more like a precise explanation of what the program was actually saying.
