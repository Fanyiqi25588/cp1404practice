"""
CP1404 Practical - Playing the Guitars (not really)
"""

import csv
from guitar import Guitar


FILENAME = "guitars.csv"


def main():
    print("My guitars!")

    guitars = load_guitars(FILENAME)

    if guitars:
        print("\nExisting guitars:")
        display_guitars(guitars)
    else:
        print("\nNo guitars found.")

    guitars.extend(get_new_guitars())

    guitars.sort()

    print("\nSorted guitars:")
    display_guitars(guitars)

    save_guitars(FILENAME, guitars)
    print("\nGuitars saved to file.")


def load_guitars(filename):
    guitars = []
    try:
        with open(filename, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                name, year, cost = row[0], int(row[1]), float(row[2])
                guitars.append(Guitar(name, year, cost))
    except FileNotFoundError:
        print(f"Warning: {filename} not found. Starting with an empty list.")
    return guitars


def display_guitars(guitars):
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


def get_new_guitars():
    new_guitars = []
    while True:
        name = input("Enter guitar name (or press Enter to stop): ")
        if not name:
            break
        year = int(input("Enter year: "))
        cost = float(input("Enter cost: $"))

        new_guitar = Guitar(name, year, cost)
        new_guitars.append(new_guitar)
        print(f"{new_guitar} added.\n")

    return new_guitars


def save_guitars(filename, guitars):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


if __name__ == "__main__":
    main()
