"""
CP1404/CP5632 Practical
File and class example - opens/reads a file, stores in objects of custom class
(contains multiple versions for demonstration: using csv and namedtuple)
"""

import csv
from collections import namedtuple
from programming_language import ProgrammingLanguage


def main():
    """Read file of programming language details, save as objects, display."""
    languages = []

    # Open the file for reading
    with open('languages.csv', 'r') as in_file:
        # Read and ignore the header line
        in_file.readline()

        # Process each line in the file
        for line in in_file:

            parts = line.strip().split(',')

            name = parts[0]
            typing = parts[1]
            reflection = parts[2] == "Yes"
            year = int(parts[3])
            pointer_arithmetic = parts[4] == "Yes"

            language = ProgrammingLanguage(name, typing, reflection, year, pointer_arithmetic)
            languages.append(language)

    for language in languages:
        print(language)



def using_csv():
    """Language file reader version using the csv module."""
    with open('languages.csv', 'r', newline='') as in_file:
        in_file.readline()
        reader = csv.reader(in_file)

        for row in reader:
            print(row)


def using_namedtuple():
    """Language file reader version using a named tuple."""
    with open('languages.csv', 'r', newline='') as in_file:
        file_field_names = in_file.readline().strip().split(',')
        print(file_field_names)

        Language = namedtuple('Language', 'name, typing, reflection, year, pointer_arithmetic')
        reader = csv.reader(in_file)

        for row in reader:
            language = Language._make(row)
            print(repr(language))


def using_csv_namedtuple():
    """Language file reader version using both csv module and named tuple."""
    Language = namedtuple('Language', 'name, typing, reflection, year, pointer_arithmetic')

    with open("languages.csv", "r") as in_file:
        in_file.readline()
        for language in map(Language._make, csv.reader(in_file)):
            print(language.name, 'was released in', language.year)
            print(repr(language))


if __name__ == "__main__":
    main()

