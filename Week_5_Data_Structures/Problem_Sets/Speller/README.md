# Speller

## What it does

Speller implements a dictionary-backed spell checker. It loads a word list, checks every word in a text, reports misspellings, and measures the performance of loading, checking, sizing, and unloading.

The `keys/` and `texts/` directories contain dictionaries and sample texts used for testing.

## Compile

```bash
make speller
```

## Use

```bash
./speller keys/aca.txt texts/her.txt
```

The command uses the selected dictionary to check the supplied text file.
