from cs50 import get_int

# Keep asking until valid
while True:
    height = get_int("Height: ")
    if 1 <= height <= 8:
        break

# Build pyramid
for i in range(1, height + 1):
    spaces = height - i
    blocks = i
    print(" " * spaces + "#" * blocks)
