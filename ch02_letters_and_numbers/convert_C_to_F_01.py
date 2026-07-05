# DESCRIPTION: A program that converts Celsius to Fahrenheit

celsius = input('Enter a temperature in Celsius: ')
celsius = float(celsius) # casting user input as a float
fahrenheit = (celsius) * float(1.8) + float(32)

print('')
print(f"{celsius} degrees Celsius is {fahrenheit} degrees Fahrenheit.")