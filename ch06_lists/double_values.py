# DESCRIPTION: User will add numbers to list and they will output list naturally, then sorted, then doubled


# First, let's figure out how many numbers the user will be entering:
size = int(input('How many numbers will you be entering? '))

# Next let's make a list. It's OK if the list doesn't have a length
# yet as we will just be appending to it.
numbers = []
double_numbers = []

# Guess we'll need a loop to populate the loop:
while len(numbers) < size:

    # Here's the tricky part. Stay with me! We have to ask the user to
    # input a number using the `input` function. Then we have to cast
    # it to an `int` before we append it. Otherwise, the list `numbers`
    # will be full of `strings`!
    num = int(input('What is number? '))
    numbers.append(num)


# Empty line for visual break
print()

print("ORIGINAL -          ", numbers)

numbers.sort()
print("ORIGINAL (sorted) - ", numbers)

# new_list = [] ## excluded code
double_numbers = [x * 2 for x in numbers]
# double_numbers = [(numbers * 2)] ## excluded code
print("DOUBLED -           ", double_numbers)