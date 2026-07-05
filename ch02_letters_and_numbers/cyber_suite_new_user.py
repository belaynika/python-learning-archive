# DESCRIPTION: Account creation program

name = input("Please enter your name: ")
user_id = input("Please enter your user id: ")
password = input("Please enter your password: ")
print('')

print(f"Welcome, {name}. Your ID is {user_id}.")
print('')

print("PASSWORD: ")
print(len(password) * 'X')