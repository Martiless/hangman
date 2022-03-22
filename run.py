import random
import os
from words import words
#from enum import Enum

# class Colors(Enum):
#RED = 1
#GREEN = 2
#BLUE = 3
#YELLOW = 4
#PURPLE = 5


#print(f'{Colors.PURPLE} This is purple, {Colors.RED} This is red, {Colors.BLUE} This is blue, {Colors.YELLOW} this is yellow and {Colors.GREEN} this is green')

def clear_screen():
    """ Clears the screen after the instructions and if the user restarts the game"""
    os.system(cls)


def welcome_message():
    """ Welcome message for users"""
    name = input('Please enter your name\n')
    print(f'Welcome {name}\n')
    print("GAME RULES:\n")
    print('Your guess has to be a valid letter')
    print('You will have 7 attemps to guess the correct letters')
    print('Each correct letter guessed will appear in the answer area')
    print('You will be notified if you guess a letter you already guessed')
    print('NOW! LETS PLAY THE GAME!')


welcome_message()


def pick_word():
    """This will randomly pick a word from a list of words"""
    word = random.choice(words)
    return word.lower()  # will return all words in lower case


def start_game():
    clear_screen()
    word = pick_word()
    answer_area = "_" * len(word)
    lives = 7
    letters_guessed = []
    print('Lets start the game')
    print(answer_area)

    while lives > 0:

     guesses = input('Please guess a letter\n')

    if guesses in word:
        print(f'Woohoo {guesses} is correct.')
        letters_guessed.append(guesses)
    elif:
        print(f"Sorry, {guesses} isn't correct, try again")
        letters_guessed.append(guesses)



def check_input():
     """
     This is to make sure the user is providing only one letter at a time
     """
     try:
        if len(values) != 1:
            raise ValueError(
                f"Exactly 1 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")


# def end_game():

# def main():
# welcome_message()
