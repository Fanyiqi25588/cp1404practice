from silver_service_taxi import SilverServiceTaxi

def main():
    silver_taxi = SilverServiceTaxi("Hummer", 200, 2)

    silver_taxi.drive(18)
    fare = silver_taxi.get_fare()

    print(silver_taxi)
    print(f"Fare: ${fare:.2f}")

    assert round(fare, 2) == 48.78, f"Expected fare to be 48.78 but got {fare:.2f}"


if __name__ == "__main__":
    main()
