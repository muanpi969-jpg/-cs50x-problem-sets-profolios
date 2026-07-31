# Filter

## What it does

This image-processing program applies grayscale, sepia, reflection, and blur transformations to bitmap images. The implementation uses pixel-level access and helper functions.

## Compile

The included Makefile builds the program:

```bash
make filter
```

## Use

```bash
./filter -g input.bmp output.bmp
```

Use `-g`, `-s`, `-r`, or `-b` for grayscale, sepia, reflection, or blur respectively. The original helper implementation is also preserved as `helper.c`.
