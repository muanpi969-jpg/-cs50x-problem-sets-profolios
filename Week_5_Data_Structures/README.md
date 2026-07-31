# Week 5 — Data Structures

## Overview & Tech Stack

Week 5 introduces abstract data types, queues, stacks, linked lists, trees, binary search trees, hash tables, and tries. The emphasis is on choosing a structure that makes the required operations efficient and understandable.

**Tech stack:** C, structs, pointers, dynamic allocation, linked data structures, hash functions, file I/O, `clang`, and `make`.

## Problem Sets Breakdown

- **Inheritance** — `inheritance.c` builds a family tree with dynamically allocated parent pointers, assigns alleles through recursive generation rules, prints each generation, and frees the allocated tree afterward.
- **Speller** — `speller.c` loads a dictionary, checks words from a text file, counts misspellings, measures each phase, and unloads the structure. `dictionary.c` provides the hash-table operations, while `keys/` and `texts/` provide test data.

## Challenges & Reflections

I had to stop thinking of a linked structure as a collection of independent variables. Every node carries ownership responsibilities, so a small mistake in a pointer update can lose an entire chain or leak memory. Speller made the performance trade-off visible: a dictionary can be correct but frustratingly slow if the hash function distributes words poorly. The most useful lesson was that data structures are not academic decorations—the structure directly determines what the program has to do for every lookup.
