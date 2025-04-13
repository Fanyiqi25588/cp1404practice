"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between.

    >>> repeat_string("hi", 1)
    'hi'
    >>> repeat_string("hi", 2)
    'hihi'
    """
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in

    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def format_phrase(phrase):
    """
    Format a phrase as a sentence: capitalize first letter and ensure single full stop.

    >>> format_phrase('hello')
    'Hello.'
    >>> format_phrase('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_phrase('nice weather')
    'Nice weather.'
    """
    phrase = phrase.strip().capitalize()
    if not phrase.endswith('.'):
        phrase += '.'
    return phrase


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should now pass
    assert repeat_string("hi", 2) == "hi hi"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    car_with_fuel = Car(fuel=10)
    assert car_with_fuel.fuel == 10, "Car did not set fuel correctly"

    car_default = Car()
    assert car_default.fuel == 0, "Car did not set default fuel to 0"


run_tests()

doctest.testmod()
