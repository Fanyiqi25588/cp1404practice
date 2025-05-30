"""
CP1404 Practical - Guitar Class

Estimate time: 20 minutes
Actual time: 18 minutes
"""

import datetime


class Guitar:

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        current_year = datetime.datetime.now().year
        return current_year - self.year

    def is_vintage(self):
        return self.get_age() >= 50
