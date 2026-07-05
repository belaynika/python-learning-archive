# DESCRIPTION: Making a program that rolls 2 dice

import random

def main():
    roll_die()

def roll_die():

    user_number = int(input("Enter a seed for the random number generation: "))
    
    random.seed(user_number)
    die_one = random.randint(1, 6)
    die_two = random.randint(1, 6)

    print("Die roll one is ", die_one, "\nDie roll two is ", die_two)
main()
