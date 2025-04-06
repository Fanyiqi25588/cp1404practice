from unreliable_car import UnreliableCar

def main():
    reliable_car = UnreliableCar("Almost Always Works", 100, 90.0)
    unreliable_car = UnreliableCar("Rarely Works", 100, 10.0)

    print("Testing reliable car (90% chance of working):")
    total_distance_reliable = 0
    for i in range(10):
        distance = reliable_car.drive(10)
        total_distance_reliable += distance
        print(f"Attempt {i + 1}: Drove {distance}km, total = {total_distance_reliable}km")

    print("\nTesting unreliable car (10% chance of working):")
    total_distance_unreliable = 0
    for i in range(10):
        distance = unreliable_car.drive(10)
        total_distance_unreliable += distance
        print(f"Attempt {i + 1}: Drove {distance}km, total = {total_distance_unreliable}km")


if __name__ == "__main__":
    main()
