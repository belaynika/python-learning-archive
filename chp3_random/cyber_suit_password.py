# DESCRIPTION: this program makes a random password for user

import random
import string

def main():
    generate_password()

def generate_password():
    user_seed = int(input("Enter a seed for the random number generation: "))
    random.seed(user_seed)

    special = "!@#$&(),-_"

    parts = [
        random.choice(special),
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.digits),
        random.choice(special)
    ]

    password = "".join(parts)

    print("Your random password is:")
    print(password)

main()