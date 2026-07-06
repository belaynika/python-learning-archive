# DESCRIPTION:  Rearranging a list with code testing out pop and insert
# type 'EOF' to stop it



# Declare an array called `customers`.
customers = []

# Declare a variable called `driver_name` and set it equal to ''.
driver_name = ''

# Collect information from the user. The user can keep entering 
# names of drivers as they enter the DMV. Once the last driver
# is loaded into the list, the DMV employee will type 'EOF' 
# (which in computer nerdom translates to "End of File").
while driver_name != 'EOF':
    driver_name = input('Enter the name of the customer: ')

    # Need to ensure that "EOF" is not input into the system as a name!
    if driver_name != 'EOF':
        customers.append(driver_name)

print()

# Output the names
print(customers)

first_customer = customers.pop(0)

customers.append(first_customer)


print(customers)
