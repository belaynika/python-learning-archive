# DESCRIPTION: output the list that includes the numbers that were entered, the sum of the numbers, and the average.

# Declare the list called `numbers`
numbers = []

# Keep running through this `while` loop forever
while True:

    # Prompt the user for a number (or "DONE" when finished)
    user_input = input('Enter a number ("DONE" to finish): ')
    
    # If the input is "DONE", break out of the `while`` loop
    if user_input == 'DONE':
        print('\n---END OF INPUT---\n')
        break
    else:
        # Otherwise, convert the input to an `int` and append
        # it to the list called `numbers`
        numbers.append(int(user_input))

sum = sum(numbers)
avgnum = sum / len(numbers)

print(f"NUMBERS =  {numbers}")
print(f"SUM = {sum}")
print(f"AVERAGE =  {avgnum}")