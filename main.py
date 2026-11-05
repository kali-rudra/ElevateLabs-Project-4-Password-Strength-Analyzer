

import argparse
import getpass
from zxcvbn import zxcvbn
from wordlist_generator import generate_wordlist

def load_common_passwords():
    with open("data/common_passwords.txt", "r") as file:
        return {
            line.strip().casefold()
            for line in file
            if line.strip()
        }

def contains_username(password, username):
    password_lower = password.casefold()
    username_lower = username.casefold()

    if len(username_lower) >= 4 and username_lower in password_lower:
        return True

    parts = username_lower.replace(".", " ").replace("_", " ").replace("-", " ").split()

    for part in parts:
        if len(part) >= 4 and part in password_lower:
            return True

    return False


def main():
    parser = argparse.ArgumentParser(
        description="Password Strength Analyzer"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    subparsers.add_parser(
        "analyze",
        help="Analyze a password's strength"
    )

    subparsers.add_parser(
        "generate",
        help="Generate a custom wordlist"
    )

    args = parser.parse_args()

    if args.command == "analyze":
        username = input("Enter a test username: ").strip()

        while not username:
            print("Username cannot be blank. Please enter a username.")
            username = input("Enter a test username: ").strip()

        while True:
            password = getpass.getpass("Enter a test password: ")
            confirmation = getpass.getpass("Confirm password: ")

            if password == confirmation:
                if not password.strip():
                    print("Password cannot be blank. Please try again.")
                    continue

                result = zxcvbn(password)
                score = result["score"]

                common_passwords = load_common_passwords()
                is_common = password.casefold() in common_passwords
                username_match = contains_username(password, username)


                if is_common or len(password) < 8 or score <= 1:
                    classification = "Weak"
                elif score == 2 or len(password) < 14 or username_match:
                    classification = "Moderate"
                else:
                    classification = "Strong candidate"

                if username_match:
                    print("Warning: Password contains a meaningful part of the username.")

                print("Raw strength score:", score, "out of 4")
                print("Preliminary classification:", classification)
                break

            print("Entries do not match. Please try again.")

    elif args.command == "generate":
        generate_wordlist()

if __name__ == "__main__":
    main()
