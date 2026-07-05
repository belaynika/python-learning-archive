# DESCRIPTION: a coin toss program that randomly states heads or tails!

import random

print("===== Coin Flipper =====")

results = random.randint(0,1) # Generates 0 or 1

if results == 0:    # Heads is 0
    print("Heads")
elif results == 1:  # Tails is 1
    print("Tails")
