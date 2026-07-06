# DESCRIPTION:  A fortune telling machine !

import random

print("=======================================")
print("Welcome to the Fortune Telling Machine!")
print("=======================================")

print(" ")

print('Enter some fortunes. Type "DONE" when you are through.')

fortunes = [] # fortunes list

while True: 
   user_input = input("Enter a fortune: ")

   if user_input == 'DONE':
      break
   else: 
      fortunes.append(user_input)
print(" ")
print(random.choice(fortunes))

print(" ")

while True:
   print(" ")
   y_n = input("Another fortune (y/n)? ")
   if y_n == 'y':
      print(" ")
      print(random.choice(fortunes))
   elif y_n == 'n':
      print(" ")
      print("Thank you for using the Fortune Telling Machine!")
      print("Smash that LIKE and Subscribe button and tell your friends!")
      break
