# DESCRIPTION:  Making a password strength validator program
# scores your passwords 

import random

password = (input("Enter your password: "))


# variables to track score with variable and list
length = 0
length_score = []

uppercase = 0
uppercase_score = []

lowercase = 0
lowercase_score = [] 

numbers = 0
numbers_score = []

specials = 0
specials_score = []

special_chars = "!@#$%^&*()-_=+[]{}|;:'\",.<>/?"  # special chars so they can be detectable 

# Count characters will place variables to count in list
for char in password:
    if char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1
    elif char.isdigit():
        numbers += 1
    elif char in special_chars:
        specials += 1

# counting to add to list 
# length first
length = len(password)
if length >= 15:
   length_score.append(8)
elif length >= 8:
   length_score.append(5)
else:
   length_score.append(0)

# scoring uppercase now with move to uppercase_score list
if uppercase >= 3:
   uppercase_score.append(8)
elif uppercase >= 2:
   uppercase_score.append(4)
elif uppercase >= 1: 
   uppercase_score.append(2)
else:
   uppercase_score.append(0)

# scoring lowercase letters to move in lowercase_score list
if lowercase >= 3:
   lowercase_score.append(8)
elif lowercase >= 2:
   lowercase_score.append(4)
elif lowercase >= 1: 
   lowercase_score.append(2)
else:
   lowercase_score.append(0)

# scoring numbers to move in numbers_score list
if numbers >= 3:
   numbers_score.append(8)
elif numbers >= 2:
   numbers_score.append(4)
elif numbers >= 1:
   numbers_score.append(2)
else:
   numbers_score.append(0)

# scoring specials to move in specials_score list
if specials >= 3:
   specials_score.append(8)
elif specials >= 2:
   specials_score.append(4)
elif specials >= 1:
   specials_score.append(2)
else:
   specials_score.append(0)

# extract values from lists
len_pts = sum(length_score)
upper_pts = sum(uppercase_score)
lower_pts = sum(lowercase_score)
num_pts = sum(numbers_score)
spec_pts = sum(specials_score)

# total score
total_score = (len_pts + upper_pts + lower_pts + num_pts + spec_pts) / 40
strength_percent = (total_score) * 100

print("\nPassword Analysis Report")
print("-------------------------")
print(f"LENGTH: {len_pts} points ({length} characters)")
print(f"UPPERCASE: {upper_pts} points ({uppercase} uppercase letter(s))")
print(f"LOWERCASE: {lower_pts} points ({lowercase} lowercase letter(s))")
print(f"NUMBERS: {num_pts} points ({numbers} number(s))")
print(f"SPECIAL CHARACTERS: {spec_pts} points ({specials} special character(s))")
print()
print(f"Total Score: {total_score:.3f}")  # format specifiers added to f-string make a decimal 
print(f"Strength Percentage: {strength_percent:.1f}%")