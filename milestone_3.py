import random

# Step 1 : list of 5 favourite fruits 
word_list = ['mango', 'soursop', 'guinep', 'guava',\
                    'starapple']
# for fruit in word_list:
#     print(fruit)

word = random.choice(word_list)
# seeding random.choice generator
random.seed(11)

# printing out word chosen random using random.choice
# print(f"This is the random word {word}")



"""
Task 1: Iteratively check if the user input is a valid guess


Write code that will continuously ask the user for a letter and validate it.


Create a new script called milestone_3.py. This file will contain the code for this milestone.


Step 1:
Create a while loop and set the condition to True. Setting the condition to True ensures that the code runs continuously.

In the body of the loop, write the code required for the following steps.


Step 2:
Ask the user to guess a letter and assign this to a variable called guess.


Step 3:
Check that the guess is a single alphabetical character. Hint: You can use Python's isalpha method to check if the guess is alphabetical.


Step 4:
If the guess passes the checks, break out of the loop.


Step 5:
If the guess does not pass the checks, then print a message saying "Invalid letter. Please, enter a single alphabetical character."


"""
# while True:
#     guess = input("Please enter a letter to play hangman: ")
#     if len(guess) == 1 and guess.isalpha():
#         break
#     else: 
#         print("Invalid letter. Please, enter a single alphabetical character.")

"""
Task 2: Check whether the guess (letter) is in the word 

Check whether the letter guessed by the user is in the secret word that was randomly chosen by the computer.
For example, if the user guesses the letter "a" and the secret word is "apple", then your code should check if "a" is in "apple".


Step 1:
Create an if statement that checks if the guess is in the word.


Step 2:
In the body of the if statement, print a message saying "Good guess! {guess} is in the word.". Obviously, format the string to show the actual guess instead of {guess}.


Step 3:
Create an else block that prints a message saying "Sorry, {guess} is not in the word. Try again." This block of code will run if the guess is not in the word.

"""
# checking if the user input (guess letter) is in the word chosen by the computer
# if the guess is one of the letters in the word chosen by the computer print 
# "Good guess! {guess} is in the word."
# else: "Sorry, {guess} is not in the word. Try again." 
# if guess in list(word):
#     print("Good guess! {guess} is in the word.")
# else: 
#     print("Sorry, {guess} is not in the word. Try again." )

"""
Task 3: Create functions to run the checks 
Good job so far!
But your code probably doesn't look great.
It's hard to tell which lines do what.


Create 2 functions, check_guess and ask_for_input functions which contain the code for those two things.


The check_guess function will take the guessed letter as an argument and check if the letter is in the word.


Step 1:
Define a function called check_guess. pass in the guess as a parameter for the function.
Write the code for the following steps in the body of this function.


Step 2:
Convert the guess into lower case.


Step 3:
Move the code that you wrote to check if the guess is in the word into this function block.


The ask_for_input function.


Step 1:
Define a function called ask_for_input.


Step 2:
Move the code that you wrote in the Iteratively check if the input is a valid guess task into this function block.


Step 3:
Outside the while loop, but within this function, call the check_guess function to check if the guess is in the word. Don't forget to pass in the guess as an argument to the method.


Step 4:
Outside the function, call the ask_for_input function to test your code.

"""

def check_guess(guess: str) -> None:
    """
    A function to check if the user input (guess) is in the word
    picked at random by the computer
    Args:
        guess (str): user input guess

    """
    # converting guess to lowercase
    guess = guess.lower()
    if guess in list(word):
        print("Good guess! {guess} is in the word.")
    else: 
        print("Sorry, {guess} is not in the word. Try again." )

    return None

def ask_for_input() -> None:
    """
    """
    while True:
        guess = input("Please enter a letter to play hangman: ")
        if len(guess) == 1 and guess.isalpha():
            break
        else: 
            print("Invalid letter. Please, enter a single alphabetical character.")
    # calling check_guess
    check_guess(guess)

    return None

ask_for_input()
