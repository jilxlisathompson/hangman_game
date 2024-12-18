# Hangman Game

## Table of Contents 
1. Objective 
2. Setup 
    - Word Selection 
    - Drawing Area
    - Guesses
3. Rules 
    - Letter Guesses 
    - Incorrect Guesses
    - Winning the Game 
    - Losing the Game 
    - No Repeated Guesses
4. What I have learned
5. Instructions on Usage
6. File Structure 
7. License Information 

## Objective 
The goal of a Hangman game is to guess a secret word (or phrase) one letter at a time before the drawing of the hangman is completed 

## Setup 
### 1. Word Selection 
- one player (the host) thinks of a secret word or phrase and writes down blanks representing each letter 
- e.g. APPLE is displayed as _ _ _ _ _ 

### 2. Drawing Area 
- A scaffold is drawn to represent the hangman,which will be gradually completed with each  incorrect guess.

### 3. Guesses
- the other player(s) try to guess the word by suggesting one letter at a time. 

## Rules
### 1. Letter Guesses
- Players guess one letter at a time. 
- If the letter is in the word, the host fills in all occurences of that letter. 
- example guessing "P" in "APPLE" updates the display to _ P P _ _ 
- if the letter in not in the word, the host adds a part to the hangman drawing i.e. head, body, arms, legs
### 2. Incorrect Guesses
- the number of incorrect guesses allowed varies, but it usually corresponds to the number of parts in the hangman drawing usually 6 or 7 parts, head, body, two arms, two legs, and sometimes a face or base 
### 3. Winning the Game 
- the player wins if they guess all the letters of the word before the hangman drawing is completed 
### 4. Losing the Game
- the player loses if the hangman drawing is completed before they guess the word.
### 5. No Repeated Guesses
- Players cannot guess the same letter more than once. If htey do, they lose a turn.

## What I have learnt 
Through this project, I have gained a comprehensive understanding of several core Python concepts, including:

- Classes: I have learned how to define, instantiate, and use classes effectively in Python. I also explored the principles of object-oriented programming (OOP) such as encapsulation and state management.
- Game Structure: I have acquired the skills necessary to structure and build a simple game from the ground up. This includes handling game logic, user input, and real-time feedback.
- Code Structure: I have learned how to organize my code from initial conception to production. This involved creating reusable functions and organizing the project into multiple files for clarity and maintainability.
- Inheritance: I explored the concept of inheritance in Python, allowing classes to derive attributes and behaviors from other classes, improving code reuse and reducing redundancy.
- Exception Handling: I have become proficient in handling potential errors or edge cases using try, except, and finally, ensuring the program runs smoothly even when unexpected input or conditions arise.
## Instructions on Usage
To use the Hangman game, follow these steps:

1. Ensure you have Python 3.x installed on your machine.
2. Download the milestone_5.py file, which contains the full implementation of the game.
3. Refer to the usage example provided at the end of the milestone_5.py file.
5. Follow the instructions there exactly, and the game should run without issues.

Make sure to provide a list of words (such as a list of strings) as input, which will be used in the game. The game will run in the terminal, allowing you to guess letters and try to solve the word. I have used the nltk library since it contains all the words in the english dictionary to make the game more fun. Feel free to do so.
## File Structure 
The project is organized as follows:

- milestone_5.py: This file contains the complete implementation of the Hangman game, including game logic, functions, and classes.
- Preceding files milstone_1.py - milestone_4.py: These files contain modular code that was developed during the game creation process, helping to build the functionality found in milestone_5.py. These might include helper functions, configuration settings, or utilities that were refactored for clarity and reusability.


## License Information 
This project is licensed under Creative Commons Licensing. You are free to share, remix, and adapt the content for non-commercial purposes, as long as appropriate credit is given. For full details, please refer to the terms outlined in the associated license documentation.

