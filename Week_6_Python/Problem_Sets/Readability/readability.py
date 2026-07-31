from cs50 import get_string

text = get_string("Text: ")

letters = 0
words = 0
sentences = 0

# Count letters
for char in text:
    if char.isalpha():
        letters += 1

# Count words
words = len(text.split())

# Count sentences
for char in text:
    if char in [".", "!", "?"]:
        sentences += 1

# Coleman-Liau formula
L = (letters / words) * 100
S = (sentences / words) * 100

index = round(0.0588 * L - 0.296 * S - 15.8)

# Output result
if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print(f"Grade {index}")
