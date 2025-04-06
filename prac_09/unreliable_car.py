import random
from car import Car

class UnreliableCar(Car):
    """A Car that may not always drive when asked, based on reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar with name, fuel and reliability."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Attempt to drive the car. Succeeds based on reliability."""
        chance = random.uniform(0, 100)
        if chance < self.reliability:
            return super().drive(distance)
        else:
            return 0
