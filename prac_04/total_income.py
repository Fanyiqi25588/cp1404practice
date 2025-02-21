def main():
    num_months = int(input("How many months? "))
    incomes = []
    for month in range(1, num_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)
    print_income_report(incomes)


def print_income_report(incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for i, income in enumerate(incomes, start=1):
        total += income
        print(f"Month {i:2} - Income: ${income:10.2f} Total: ${total:10.2f}")

main()
