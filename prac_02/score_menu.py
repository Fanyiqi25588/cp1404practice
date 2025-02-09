def get_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    return '*' * int(score)


def get_valid_score():
    while True:
        try:
            score = float(input("Enter score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid input. Score must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    score = get_valid_score()
    while True:
        print("\nMenu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = input(">>> ").upper()

        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(get_result(score))
        elif choice == "S":
            print(show_stars(score))
        elif choice == "Q":
            print("Farewell!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
