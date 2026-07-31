# Week 2 — Arrays

## Overview & Tech Stack

Week 2 moves from basic C syntax into preprocessing, compilation, linking, debugging, arrays, strings, command-line arguments, and introductory cryptography.

**Tech stack:** C, fixed-size arrays, character classification from `<ctype.h>`, string functions, `clang`, the CS50 library, and `libm` for mathematical rounding.

## Problem Sets Breakdown

- **Readability** — `readability.c` scans a passage, counts alphabetic characters, spaces, and sentence-ending punctuation, then computes the Coleman–Liau index using letters and sentences per 100 words.
- **Scrabble** — `scrabble.c` stores the 26 letter values in an array, normalizes each alphabetic character with `toupper`, looks up its point value, and compares the two players' totals.
- **Substitution** — `substitution.c` validates a 26-character key with a Boolean `seen` array, then maps plaintext characters to ciphertext while preserving case and leaving punctuation unchanged.
- **Lecture practice** — `score.c` calculates an average from three hard-coded scores. It is a useful precursor to replacing repeated variables with an array.

## Challenges & Reflections

I had to be careful not to confuse a string's length with the number of meaningful words in it. Counting spaces works for the simple coursework inputs, but it made me think about edge cases such as repeated spaces and punctuation. The Substitution exercise was the first time I used an auxiliary array to enforce an input invariant, and that was a turning point: validation became a design problem rather than a collection of afterthoughts.
