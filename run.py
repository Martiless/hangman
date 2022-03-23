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
    clear_screen() #clears the inital instructions from the screen once the game starts
    word = pick_word()
    answer_area = "_" * len(word) #creates an area of underscores that equal the lenght of the word
    lives = 7
    letters_guessed = [] #empty list to add the guessed letters to once they are inputted 
    print('Lets start the game')
    print(answer_area)

    while lives > 0:

     guesses = input('Please guess a letter\n')
     
     if guesses in word:
         print(f'Woohoo {guesses} is correct.')
         letters_guessed.append(guesses)
     else:
         lives = lives - 1
         print(f"Sorry, {guesses} isn't correct. You have {lives} lives left. Guess again")
         letters_guessed.append(guesses)

    for letter in word:
        if letter in letters_guessed:
            print(f'{letter}')
        else:
            print("_")


def play():
    game = input('Please enter Y or N \n')
    if game == 'Y':
        start_game()
    elif game == 'N':
        print(f'Sorry to see you go so soon {name}')
    else:
        print('Please enter a valid answer')
        play()





#def check_input():
  #   """
 #    This is to make sure the user is providing only one letter at a time
 #    """
 #    try:
  #      if len(values) != 1:
  #          raise ValueError(
  #              f"Exactly 1 values required, you provided {len(values)}"
  #          )
  #  except ValueError as e:
  #      print(f"Invalid data: {e}, please try again.\n")


# def end_game():

def main():
    welcome_message()
    play()
    #start_game()

main()

