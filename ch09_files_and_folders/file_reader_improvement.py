# DESCRIPTION: exploring file reading (I have file_reader.py already but this is a remix with more functional code)
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
    filename = input("File name? ")
    print("")

# Finds file based on input and gives error if not found
    try: 
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("That file does not exist.")

main()