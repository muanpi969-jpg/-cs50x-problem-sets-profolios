import csv
import sys


def main():

    # Check arguments
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)

    # Read database
    database = []
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        strs = reader.fieldnames[1:]  # STR names
        for row in reader:
            database.append(row)

    # Read DNA sequence
    with open(sys.argv[2]) as file:
        sequence = file.read()

    # Find STR counts in sequence
    counts = {}
    for STR in strs:
        counts[STR] = longest_match(sequence, STR)

    # Compare against database
    for person in database:
        match = True
        for STR in strs:
            if int(person[STR]) != counts[STR]:
                match = False
                break
        if match:
            print(person["name"])
            return

    print("No match")


def longest_match(sequence, subsequence):
    longest_run = 0
    sub_len = len(subsequence)
    seq_len = len(sequence)

    for i in range(seq_len):
        count = 0

        while True:
            start = i + count * sub_len
            end = start + sub_len
            if sequence[start:end] == subsequence:
                count += 1
            else:
                break

        longest_run = max(longest_run, count)

    return longest_run


if __name__ == "__main__":
    main()
