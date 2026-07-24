# DESCRIPTION: exploring file reading 
# options: file01.txt / file02.txt / file03.txt 

# note: You need to type --> "cd ch09_files_and_folders" to access txt file 


def main():
    file_reader()

def file_reader():
    '''
    This function will ask the user to input a file name. The
    file will be opened and the contents will be output
    to the screen.
    '''
    user_input = input("File name? ")
    print("")

    file01 = open("file01.txt", "r")
    file02 = open("file02.txt", "r")
    file03 = open("file03.txt", "r")


    if user_input == "file01.txt":
        print(file01.read())
    if user_input == "file02.txt":
        print(file02.read())
    if user_input == "file03.txt":
        print(file03.read())
    


main()
