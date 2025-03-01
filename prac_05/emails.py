# emails.py
# Estimate time: 1 hour
# Actual time: 1 hour 10 minutes

def extract_name_from_email(email):
    """Extracts the name part from an email address."""
    name_part = email.split('@')[0]
    name_parts = name_part.split('.')
    return ' '.join(name_parts).title()

def main():
    email_to_name = {}

    while True:
        email = input("Email: ").strip()
        if not email:
            break

        name = extract_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()

        if confirmation not in ['n', 'no']:
            email_to_name[email] = name
        else:
            name = input("Name: ").strip()
            email_to_name[email] = name

    for email, name in email_to_name.items():
        print(f"{name} ({email})")

    main()
