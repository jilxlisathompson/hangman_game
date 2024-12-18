"""
Task 1: Creat the Class

Create a new script called milestone_4.py. This file will contain the code for the third milestone.

Define the __init__ method of the Hangman class.


Step 1:
Create a class called Hangman.


Step 2:
Inside the class, create an __init__ method to initialise the attributes of the class.

Pass in word_list and num_lives as parameters. Make num_lives a default parameter and set the value to 5.


Step 3:
Initialise the following attributes:

word: The word to be guessed, picked randomly from the word_list. Remember to import the random module into your script
word_guessed: list - A list of the letters of the word, with _ for each letter not yet guessed. For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']. If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
num_letters: int - The number of UNIQUE letters in the word that have not been guessed yet
num_lives: int - The number of lives the player has at the start of the game.
word_list: list - A list of words
list_of_guesses: list - A list of the guesses that have already been tried. Set this to an empty list initially

"""
import random
from nltk.corpus import words
import nltk

class Hangman:
    def __init__(self, word_list: list, num_lives: int = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = None  # The word to guess
        self.word_guessed = []  # List of guessed letters (e.g., ['_', '_', '_', '_'])
        self.num_letters = 0  # The number of unique letters to guess
        self.list_of_guesses = []  # List of guessed letters
        self.guess = None  # User's guess
    
    def get_num_letters(self):
        return self.num_letters

    def word_guess_blanks(self):
        """Initializes the word_guessed list with underscores for each letter in the word."""
        self.word_guessed = [' _ '] * len(self.word)
        return self.word_guessed

    def random_word_choice(self) -> str:
        """Randomly selects a word from the word_list."""
        random.seed(11)  # Optional: for reproducibility
        self.word = random.choice(self.word_list)
        # Update num_letters to be the number of unique letters in the word
        self.num_letters = len(set(self.word))
        return self.word

    def check_guess(self, guess) -> None:
        """Checks if the user's guess is in the word, and replaces it in word_guessed if found."""
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            
            # Keep track of which letters have been replaced
            seen = set()  # A set to keep track of letters that have already been replaced
            
            # Iterate over all positions in self.word
            for index, letter in enumerate(self.word):
                if letter == guess:
                    # Update word_guessed if the letter matches the guess
                    self.word_guessed[index] = guess
                    seen.add(letter)  # Mark this letter as replaced

            # Decrease the number of unique letters to guess
            self.num_letters -= 1

            # # Check if the player has guessed all the unique letters
            if self.num_letters == 0:
                print("Congratulations! You've guessed the word!")
                return True  # Game over, player won
        else:
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")

        
        print("Current word: " + ''.join(self.word_guessed))
        return False  # Game continues

    def ask_for_input(self) -> None:
        """Main loop that runs the game, asking for input and checking guesses."""
        # Select the word and initialize guessed word blanks
        self.word = self.random_word_choice()
        self.word_guessed = self.word_guess_blanks()

        while self.num_lives > 0:
            guess = input("Please enter a letter to play hangman: ").lower()

            # Validate guess
            if not len(guess) == 1 or not guess.isalpha():
                print("Invalid input. Please enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You've already guessed that letter!")
            else:
                # Add guess to list of previous guesses
                self.list_of_guesses.append(guess)

                # Check if the guess is correct
                if self.check_guess(guess):
                    break  # Player has won, exit the loop


        return None

"""
Task 5: create the logic for the code 
Create a function that will run all the code to run the game as expected. You should begin by creating a new script called milestone_5.py. Copy all the codes in milestone_4.py file into the newly created milestone_5.py file.


Step 1:
Create a function called play_game that takes word_list as a parameter. Inside the function, write the code for the following steps

Create a variable called num_lives and assign it to 5
Create an instance of the Hangman class. Do this by calling the Hangman class and assign it to a variable called game
Pass word_list and num_lives as arguments to the game object
Create a while loop and set the condition to True. In the body of the loop, do the following:
Check if the num_lives is 0. If it is, that means the game has ended and the user lost. Print a message saying 'You lost!'
Next, check if the num_letters is greater than 0. In this case, you would want to continue the game, so you need to call the ask_for_input method.
If the num_lives is not 0 and the num_letters is not greater than 0, that means the user has won the game. Print a message saying 'Congratulations. You won the game!'
Step 2:
Outside the function, call your play_game function to play your game. Don't forget to pass in your list of words as argument to the function.
"""


def play_game(word_list: list) -> None:
    num_lives = 5
    game = Hangman(word_list, num_lives)
    
    while True:
        # Check if the player has ran out of lives
        if game.num_lives == 0:
            print("Game over! You lost")
            break  # Exit the loop when lives runs out
        
        # Check if there are still letters to guess (game continues)
        if game.num_letters >= 0:
            game.ask_for_input()
        
        # Check if the player has won 
        if game.num_lives != 0 and game.num_letters == 0:
            print('Congratulations! You won the game!')
            break  # Exit the loop when the player wins
    
    return None


# nltk.download('words')
word_list = words.words()
subset_size = 50

# Get a random subset of the word list
word_list = random.sample(word_list, subset_size)

# print(word_list)
play_game(word_list)