# Recover

## What it does

`recover.c` scans a forensic memory-card image for JPEG signatures and writes each recovered image to a numbered `.jpg` file.

## Compile

```bash
clang recover.c -o recover
```

## Use

```bash
./recover card.raw
```

The program creates recovered images in the current directory.
