import random
import os 
from words import words


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
    clear_screen()


welcome_message()


def pick_word():
    word = random.choice(words)
    return word.lower()

#answer = pick_word()

def clear_screen():
    """ Clears the screen after the instructions and if the user restarts the game"""
    os.system(clr)

def start_game():


#def end_game()

# def main():
    #welcome_message()
