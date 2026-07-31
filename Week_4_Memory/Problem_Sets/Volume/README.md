# Volume

## What it does

`volume.c` adjusts the volume of a WAV audio file by multiplying each audio sample by a user-provided factor while preserving the file header.

## Compile

```bash
clang volume.c -o volume
```

## Use

```bash
./volume input.wav output.wav 2.0
```

The command writes the adjusted audio to the output file.
