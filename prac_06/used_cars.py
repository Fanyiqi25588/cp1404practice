"""
CP1404/CP5632 Practical - Client code to use the Car class.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use Car class."""
    my_car = Car("MyCar", 180)
    my_car.drive(30)
    print(f"{my_car.name} has fuel: {my_car.fuel}")
    print(my_car)

    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print(f"{limo.name} has fuel: {limo.fuel}")
    limo.drive(115)
    print(limo)

main()
