import random
import os 
from words import words

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
    return word.lower() #will return all words in lower case


def start_game(word):


#def end_game()

# def main():
    #welcome_message()