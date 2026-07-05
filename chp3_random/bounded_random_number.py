import random

def main():
    bounded_random()

def bounded_random():

    user_number = int(input("Enter a seed for the random number generation: "))

    random.seed(user_number)
    user_number = random.randint(1, 10)
    print(user_number)

main()