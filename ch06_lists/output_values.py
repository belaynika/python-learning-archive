# DESCRIPTION: User enters 5 numbers, program will sort them into a list

# Create an empty list

numbers =[]



# Walk through the list and grab a number from the
# user. Insert that number into the next available cell

for x in range(5):
    numbers.append(int(input('Enter a number: ')))

print()

# Sort the list
numbers.sort() 

# Print out the list naturally:
print(numbers)

# Print out the list in a pretty way:
print("Your numbers are:", *numbers, sep="  ")