# Week 3 — Algorithms

## Overview & Tech Stack

Week 3 focuses on linear and binary search, bubble sort, selection sort, merge sort, asymptotic notation, recursion, and the relationship between an algorithm's design and its running time.

**Tech stack:** C, structs, arrays, two-dimensional arrays, command-line arguments, `string.h`, `clang`, and benchmark data files.

## Problem Sets Breakdown

- **Plurality** — `plurality.c` stores candidate names and vote totals in an array of structs. `vote` performs a linear search to validate and record each vote, while `print_winner` makes two passes: one to find the maximum and another to print every tied candidate.
- **Runoff** — `runoff.c` stores every voter's ranking in a two-dimensional `preferences` array. Each round tabulates the highest-ranked non-eliminated candidate, checks for a majority or tie, finds the minimum, eliminates candidates, and resets vote totals before the next round.
- **Sort** — this folder contains ordered, reversed, and random benchmark inputs plus answers. The implementation itself is not present, but the data represents the comparison of sorting approaches by observed behavior and asymptotic complexity.

## Challenges & Reflections

I found Runoff harder than Plurality because the state of every candidate changes between rounds. A function could be locally correct and still produce a wrong election if another function failed to reset or interpret that state correctly. I also had to learn to trace a two-dimensional array with a concrete voter and rank instead of staring at the entire matrix. That debugging habit—reduce the algorithm to one small input—was more valuable than memorizing the names of the sorting algorithms.
