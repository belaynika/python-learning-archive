# DESCRIPTION:  making a mfa program

import random


user_seed = int(input("ENTER SEED FOR SIMULATION: "))

random.seed(user_seed)  # making a random seed
# print(user_seed)  # I am testing if my random seed worked here 

backups = [random.randint(100000, 999999) for i in range(10)] # backups will print 10 numbers that are 6 digits

print("")
print("===============================")
print("     SIMULATING CODE USE       ")
print("===============================")
print("")

for code in backups:  # This will print the backup codes 
  print(f"Backup code: {code}")

print("")
print("===============================")
print("     SIMULATING CODE USE       ")
print("===============================")
print("") 

number_of_backups = len(backups)  # counts the codes in backups list 
print(f"You have {number_of_backups} codes remaining.")

user_code = int(input("Enter a valid code: "))
print("")

if user_code in backups:
  print("Access Granted")
  print("")
  backups.remove(user_code) # removes code user used from backups list!
  number_of_backups = len(backups)  # counting the codes again for new amount of codes in backups list
  print(f"You have {number_of_backups} codes remaining.")
  print("")
  for code in backups:  # nesting to print left over mfa codes 
    print(f"Backup code: {code}")
else: 
  print("Access Denied")