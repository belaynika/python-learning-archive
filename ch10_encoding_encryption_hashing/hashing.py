# DESCRIPTION: Making a hashed message 

import hashlib

def main():
    hashing()

def hashing():

    # Ask user for message 

    user_message = input("Enter the message to hash: ")

    # Get data

    user_message_bytes = user_message.encode()

    hashed_message = hashlib.sha256(user_message_bytes)

    hash_hex = hashed_message.hexdigest()

    # Output data

    print(f"Hashed: {hash_hex}")


main()