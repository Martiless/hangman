import random
import os 


def welcome_message():
    """ Welcome message for users"""
    name = input('Please enter your name\n')
    print(f'Welcome {name} to your hangman game\n')
    print("GAME RULES:\n")
    print('Your guess has to be a valid letter\n')
    print('You will have 7 attemps to guess the correct letters\n')
    print('Each correct letter guessed will appear in the answer area\n')
    print('You will be notified if you guess a letter you already guessed\n')
    print('NOW! LETS PLAY THE GAME!')



def pick_word():
    with open('words.txt') as f:
        words = f.readlines()
        return words


#def start_game()

#def end_game()