import random
MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6

def generate_quick_picks(num_picks):
    picks = []
    for _ in range(num_picks):
        quick_pick = random.sample(range(MIN_NUMBER, MAX_NUMBER + 1), NUMBERS_PER_PICK)
        quick_pick.sort()
        picks.append(quick_pick)
    return picks

def main():
    num_picks = int(input("How many quick picks? "))
    quick_picks = generate_quick_picks(num_picks)
    for pick in quick_picks:
        print(" ".join(f"{num:2}" for num in pick))

    main()
