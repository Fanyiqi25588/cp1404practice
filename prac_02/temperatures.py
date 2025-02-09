
def convert_celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32

def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def main():
    while True:
        print("""C - Convert Celsius to Fahrenheit F - Convert Fahrenheit to Celsius Q - Quit""")
        choice = input(">>> ").upper()

        if choice == "C":
            celsius = float(input("Celsius: "))
            print(f"Result: {convert_celsius_to_fahrenheit(celsius):.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            print(f"Result: {convert_fahrenheit_to_celsius(fahrenheit):.2f} C")
        elif choice == "Q":
            break
        else:
            print("Invalid option")

    print("Thank you.")


if __name__ == "__main__":
    main()
