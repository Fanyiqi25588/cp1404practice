CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia"
}

state_code = input("Enter short state: ").strip().upper()
while state_code:
    try:
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").strip().upper()

print("\nAll states and names:")
for code, name in CODE_TO_NAME.items():
    print(f"{code:3} is {name}")
