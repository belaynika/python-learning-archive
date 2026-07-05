# DESCRIPTION: Making a random seeded number!

import random


def main():
    generate_seeded_random_number()

def generate_seeded_random_number():
    
    user_seed = int(input("Enter a seed for the random number generation: "))
    
    random.seed(user_seed)
    random_number = random.random()

    print(random_number)


main()