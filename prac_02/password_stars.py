def get_password():
    return input("Enter your password: ")
def print_asterisks(password):
    print("Password is: ", "*" * len(password))
def main():
    password = get_password()
    print_asterisks(password)
if __name__ == "__main__":
    main()
