from cs50 import get_float

# Keep asking until valid input
while True:
    dollars = get_float("Change owed: ")
    if dollars >= 0:
        break

# Convert dollars to cents (avoid floating errors)
cents = round(dollars * 100)

coins = 0

# Quarters
coins += cents // 25
cents %= 25

# Dimes
coins += cents // 10
cents %= 10

# Nickels
coins += cents // 5
cents %= 5

# Pennies
coins += cents

print(coins)
