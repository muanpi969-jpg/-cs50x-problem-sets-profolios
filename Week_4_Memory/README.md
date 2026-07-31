# Week 4 — Memory

## Overview & Tech Stack

Week 4 covers pointers, segmentation faults, dynamic memory allocation, the stack and heap, buffer overflows, file I/O, binary formats, and image processing.

**Tech stack:** C, pointers, `malloc`/`calloc`-style memory management, `FILE *`, byte-level file operations, bitmap structures, `stdint.h`, `getopt`, `clang`, and `make`.

## Problem Sets Breakdown

- **Volume** — `volume.c` reads a WAV header, copies its 44 bytes unchanged, multiplies each 16-bit audio sample by a factor, and writes the transformed stream to a new file.
- **Filter** — `filter.c` parses a filter flag, validates a 24-bit BMP header, allocates a pixel matrix, reads scanlines while accounting for padding, calls image transformations, and writes the modified pixels. `helpers.c` implements grayscale, sepia, reflection, and blur; the extra `helper.c` preserves another implementation of those transformations.
- **Recover** — `recover.c` reads a forensic image in 512-byte blocks, recognizes JPEG headers, opens numbered output files at each header, and writes subsequent blocks until the next image begins.

## Challenges & Reflections

This was the week where a program could compile and still fail immediately because I had misunderstood memory. I spent hours tracing segmentation faults back to a pointer or buffer boundary instead of the line where the crash appeared. Working with BMP padding and WAV headers also made binary files feel concrete: a few bytes of metadata determine how the rest of the file must be interpreted. I became much more disciplined about allocation, cleanup, and checking file handles before using them.
