import random

MAX_INCREASE = 0.175
MAX_DECREASE = 0.05
MIN_PRICE = 1.00
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
FILENAME = "stock_prices.txt"

price = INITIAL_PRICE
number_of_days = 0

with open(FILENAME, 'w') as out_file:
    print(f"Starting price: ${price:,.2f}", file=out_file)

    while MIN_PRICE <= price <= MAX_PRICE:
        number_of_days += 1
        price_change = random.uniform(-MAX_DECREASE, MAX_INCREASE) if random.randint(1, 2) == 1 else random.uniform(-MAX_DECREASE, 0)
        price *= (1 + price_change)

        print(f"On day {number_of_days} price is: ${price:,.2f}")
        print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)

print(f"Simulation finished. Results saved to {FILENAME}.")
