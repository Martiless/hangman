import random
import os 
import words from words


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
    with open('words.txt') as f:
        words = f.readlines()
        return words


#def start_game()

#def end_game()

# def main():
    #welcome_message()
