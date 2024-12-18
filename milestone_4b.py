import random

class Hangman:
    def __init__(self, word_list: list, num_lives: int = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = None  # The word to guess
        self.word_guessed = []  # List of guessed letters (e.g., ['_', '_', '_', '_'])
        self.num_letters = 0  # The number of unique letters to guess
        self.list_of_guesses = []  # List of guessed letters
        self.guess = None  # User's guess

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
            # if self.num_letters == 0:
            #     print("Congratulations! You've guessed the word!")
            #     return True  # Game over, player won
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

            # Deduct lives and check if the game is over
            # self.num_lives -= 1
            # if self.num_lives == 0:
            #     print("Game over! You've run out of lives.")
            #     break  # Exit the loop when out of lives

        return None

# Example usage:
game = Hangman(word_list=['mango', 'soursop', 'guinep', 'guava', 'starapple'])
game.ask_for_input()
