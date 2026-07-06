# DESCRIPTION: User can make a list and have it sorted and reversed 


# Declare the variable 'name' and give it a value of NONE
name = None

# Declare the list 'names' but keep it empty
names = []

# Here we populate the list. We will keep appending input from the user
# to the list unless the input is '_DONE_'. Note the tricky part - we 
# have to make sure we don't append '_DONE_' to the list!
while (name != '_DONE_'):
    name = input('Enter a name (enter "_DONE_" to end): ')
    if name == '_DONE_':
        break
    else:
        names.append(name)

# Empty line for visual break
print()

print("ORIGINAL - ", names)

names.sort()    
# print("SORTED - ", name.sort) ## mistake code
print("SORTED - ", names)

names.reverse()
print("REVERSED - ", names)