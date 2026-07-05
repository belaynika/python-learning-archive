# DESCRIPTION: Program asks user if they want c or f and then converts them based on choice

print("===== Temperature Converter =====")
print() 
print("  1. Convert from Celsius to Fahrenheit")
print("  2. Convert from Fahrenheit to Celsius")
print()

fahrenheit = 1 
celsius = 2

user_choice = int(input("Please choose from the above menu: "))
user_temp = float(input("Enter a temperature to convert: "))

print()

if user_choice == 1:  # IF user choose 1. Convert from Celsius to Fahrenheit this choice will determine output
  c_to_f = user_temp * 9/5 + 32 # c_to_f is the conversion sum from celsuis to farhenheit
  print(f"{user_temp} degrees Celsius is {c_to_f} degrees Fahrenheit.")
elif user_choice == 2:
  f_to_c = (user_temp - 32 ) * 5/9  # f_to_c is the conversion sum from farhenheit to celsius
  print(f"{user_temp} degrees Fahrenheit is {f_to_c} degrees Celsius.")