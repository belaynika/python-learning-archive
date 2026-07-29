# DESCRIPTION: exploring file reading 
# options: file01.txt / file02.txt / file03.txt 

# note: You need to type --> "cd ch09_files_and_folders" to access txt file 
## NEW note: Added auto directory instead

import os


def main():
    file_reader()

def file_reader():
    '''
    This function will ask the user to input a file name. The
    file will be opened and the contents will be output
    to the screen.
    '''

    # Getting directory for txt
    directory = os.path.dirname(os.path.abspath(__file__))

    # Building paths to files 
    file01_path = os.path.join(directory, "file01.txt")
    file02_path = os.path.join(directory, "file02.txt")
    file03_path = os.path.join(directory, "file03.txt")

    user_input = input("File name? ")
    print("")

    with open(file01_path, "r") as file01, \
        open(file02_path, "r") as file02, \
        open(file03_path, "r") as file03:

        if user_input == "file01.txt":
            print(file01.read())
        if user_input == "file02.txt":
            print(file02.read())
        if user_input == "file03.txt":
            print(file03.read())
    


main()
