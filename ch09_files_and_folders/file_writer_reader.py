# BRIEF DESCRIPTION:  will ask user for which file they want then they can add and close
# options: pokemon.txt / movies.txt / music.txt 

# note: You need to type --> "cd ch09_files_and_folders" to access txt file 

def main():
    writer_reader()

def writer_reader():
    '''
    This function will ask the user to type the name
    of a file. The program will open the file, ask the
    user to enter a word (or phrase), and add that input
    to the end of the file. 

    Then the file is closed.

    The file is reopened and the contents are output.
    '''
    # 1. Ask user for file name and words to add put in variables
    user_file = input("File name? ")
    user_word = input("Word to add? ")

    print("")

    # Append entry to end of txt file and close based on user_file

    if user_file == 'pokemon.txt':
        pokemonfile = open('pokemon.txt', 'a')
        pokemonfile.write(user_word + '\n')
        pokemonfile.close()
        pokemonfile = open('pokemon.txt', 'r')
        print(pokemonfile.read())
    elif user_file == 'music.txt':
        musicfile = open('music.txt', 'a')
        musicfile.write(user_word + '\n')
        musicfile.close()
        musicfile = open('music.txt', 'r')
        print(musicfile.read())
    else:
        user_file == 'movies.txt'
        moviesfile = open('movies.txt', 'a')
        moviesfile.write(user_word + '\n')
        moviesfile.close()
        moviesfile = open('movies.txt', 'r')
        print(moviesfile.read())

    

main();