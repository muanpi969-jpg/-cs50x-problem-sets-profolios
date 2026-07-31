# DNA

## What it does

`dna.py` identifies a person by comparing the longest runs of repeated short tandem repeats in a DNA sequence against a CSV database.

The `sequences/` directory contains sample DNA sequences.

## Use

```bash
python3 dna.py database.csv sequences/1.txt
```

The database CSV must contain the STR columns expected by the program.
