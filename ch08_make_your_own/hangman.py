# DESCRIPTION: program that lets you play hangman, you can pick the category and play as many times as wanted!

import random

# ASCII Art for the Hangman stages (up to 6 wrong guesses)
HANGMAN_STAGES = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    ========="""
]

# Word list bank categorized by topic
WORD_CATEGORIES = {
    "1": ("Animals", ["PYTHON", "DOLPHIN", "KANGAROO", "CHEETAH", "ELEPHANT", "PENGUIN"]),
    "2": ("Video Games", ["MINECRAFT", "ZELDA", "POKEMON", "TETRIS", "OVERWATCH", "METROID"]),
    "3": ("Movies", ["INCEPTION", "AVATAR", "GLADIATOR", "TITANIC", "INTERSTELLAR", "FROZEN"])
}

# function for picking the category 
def pick_category(): 
    print("Welcome to Hangman!")
    print("The rules are simple. You have 6 guesses. Guess the right word and you win! Guess the wrong word...")
    print("")
    print("Please pick a word category")
    print("Options: ")
    print(" 1. Animals ")
    print(" 2. Video Games")
    print(" 3. Movies")

    # input validation grabs from word_catagories list and picks random word from topics depending on which user chooses
    while True:
    # user_choice = int(input("Which category would you like?: ")) # creates key error when calling pick_category()
        user_choice = input("Which category would you like?: ").strip() # strip cleans up invisible space that was crashing program
        if user_choice in WORD_CATEGORIES:
            category_data = WORD_CATEGORIES[user_choice]
            word_list = category_data[1]
            return random.choice(word_list)
            # break
        print("Invalid choice! Please enter 1, 2, or 3.")

    # category_data = WORD_CATEGORIES[user_choice]
    # word_list = category_data[1]


    # hangman_word = random.choice(word_list)
    # return hangman_word

# print("Secret word chosen:", pick_category()) # DEBUG

# function for word blanks display string showing guessed letters and underscores for unguessed ones
def display_word(secret_word, guessed_letters):
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " " 
        else: 
            display += "_ "             
    
    print("Word:", display)


# guessed = ["P", "O"]  # DEBUG
# display_word("PYTHON", guessed) # DEBUG

# function for input validation while user tries to guess a number or guesses the same letter and error message will show
def get_guess(guessed_letters):
    while True:
        guess = input("Guess a letter: ").upper().strip() 

        if len(guess) != 1:
            print("Please enter only ONE letter!")
        elif not guess.isalpha():   
            print("Please enter an actual letter (A-Z)!")
        elif guess in guessed_letters:
            print("You already guessed that letter!")
        else: 
            return guess

# function for main game this calls stored functions from picks, guesses, secret word, and uses hangman stages list
def play_game(): 
    secret_word = pick_category()
    guessed_letters = [] 
    wrong_guesses = 0 
    max_wrong = 6 # 6 hangman stages 

    while wrong_guesses < max_wrong: 
        print(HANGMAN_STAGES[wrong_guesses])
        display_word(secret_word, guessed_letters)

        guess = get_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in secret_word:
            print("Good guess!")
        else:
            print("Wrong!")
            wrong_guesses += 1

        if all(letter in guessed_letters for letter in secret_word):
            print("You win! The word was:", secret_word)
            return 
    
    print(HANGMAN_STAGES[max_wrong])
    print("Game over! The word was", secret_word)

play_game()

# asks user if they want to play again if so function play_game() is called and restarts
while True:
   print(" ")
   y_n = input("Would you like to play again (y/n)? ")
   if y_n == 'y':
      print(" ")
      play_game()
   elif y_n == 'n':
      print(" ")
      print("Thank you for playing!")
      break
   