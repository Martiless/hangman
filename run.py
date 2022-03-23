import random
import os
from words import words
import time 
#from enum import Enum

# class Colors(Enum):
#RED = 1
#GREEN = 2
#BLUE = 3
#YELLOW = 4
#PURPLE = 5

#print(f'{Colors.PURPLE} This is purple, {Colors.RED} This is red, {Colors.BLUE} This is blue, {Colors.YELLOW} this is yellow and {Colors.GREEN} this is green')


def clearConsole():
    """ 
    Checks to see what os if the computer is running Windows
    This piece of code was taken from www.delfstack.com"""
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def clear_screen():
    """ Clears the screen after the instructions and if the user restarts the game"""
    os.system('cls')
    clearConsole()

def welcome_message():
    """ Welcome message for users"""
    print('Welcome to Hangman\n')
    print("GAME RULES:\n")
    print('Your guess has to be a valid letter')
    print('You will have 7 attemps to guess the correct letters')
    print('Each correct letter guessed will appear in the answer area')
    print('You will be notified if you guess a letter you already guessed')
    name = input('Please enter a name:\n')
    print(f'Hello {name}, would you like to play a game?\n')


def pick_word():
    """This will randomly pick a word from a list of words"""
    word = random.choice(words)
    return word.lower()  # will return all words in lower case

def start_game():
    """
    This starts the game once the user has entered a name 
    """
    #clears the inital instructions from the screen once the game starts
    clear_screen()
    word = pick_word()
    #creates area of underscores that equals lenght of the word
    answer_area = "_" * len(word)
    #empty list to add the guessed letters to once they are inputted 
    letters_guessed = []
    correct_answer = False
    lives = 7
    print('Lets start the game\n')
    print(answer_area)

    #if lives is more than 0 and correct_answer is false the loop will keep running
    while lives > 0 and not correct_answer:

     guesses = input('Please guess a letter\n')
     #checks if the guess is only 1 letter and is in the alphabet
     if len(guesses) == 1 and guesses.isalpha():
         if guesses in word:
             print(f'Woohoo {guesses} is correct.')
             #add the guess to a list of letters
             letters_guessed.append(guesses)
             answer_area = guesses.join(answer_area)
         elif guesses in letters_guessed:
             print(f'You have already guessed {guesses}, try again!')
         else:
             lives = lives - 1
             print(f"Sorry, {guesses} isn't correct. You have {lives} lives left. Guess again")
             letters_guessed.append(guesses)

     else:
         print('Not a valid letter. Try again :)')
     print(answer_area)

    if correct_answer == True:
        print('Woohoo you guessed the word! Winner!!')
    else:
        print(f'You are out of lives, sorry about that. The word was {word}. Better luck next time!')
     


def play():
    """
    Asked the user if they would like to play the game and calls
    start_game if they answer yes"""
    game = input('Please enter Y or N \n')
    if game == 'Y':
        start_game()
    elif game == 'N':
        print('Sorry to see you go so soon!')
    else:
        print('Please enter a valid answer')
        play()



# def end_game():

def main():
    welcome_message()
    play()

main()

