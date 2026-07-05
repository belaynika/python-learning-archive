# DESCRIPTION: a program that converts inches to feet

inches = int(input("Enter the number of inches: "))

feet = inches // 12
remaining_inches = inches % 12
    
print(f"{inches} inches is {feet} feet, and {remaining_inches} inches") 