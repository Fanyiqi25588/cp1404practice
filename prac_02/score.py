import random

def get_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def main():
    score = float(input("Enter score: "))
    result = get_result(score)
    print(result)

    random_score = random.uniform(0, 100)
    print(f"Random score: {random_score:.2f}")
    print(get_result(random_score))

if __name__ == "__main__":
    main()
