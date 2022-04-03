import random
import gspread
from google.oauth2.service_account import Credentials
from words import words
from utils.hangman import hangman_graphic
from utils.display import Colors
from utils.display import Display


# This piece of code was taken from the CI Love Sandwiches project
# Allows other people to add words to an external sheet
# without having to touch the code

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]


CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)


def welcome_message():
    """
    Welcome message for users
    """

    print(f"""{Colors.blue}

██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
     """)
    print(f'{Colors.reset}')
    print('Welcome to Hangman\n')
    print("GAME RULES:\n")
    print('Your guess has to be a valid letter')
    print('You will have 7 attemps to guess the correct letters')
    print('Each correct letter guessed will appear in the answer area')
    print('You will be notified if you guess a letter you already guessed')
    while True:
        name = input('Please enter a name:\n')
        if not name.isalpha():
            print('Not a valid input, please try again')
        else:
            break

    print(f'Hello {name}, would you like to play a game?\n')


def pick_word():
    """
    This will randomly pick a word from a list of words
    """
    try:
        # Gets data from google sheets worksheet
        SHEET = GSPREAD_CLIENT.open('hangman_words')
        # Getting the list from the excel file
        list_of_words = SHEET.worksheet('new_words')
        lists = list_of_words.get_all_values()
        selection = random.choice(lists)
        # Converting the list to a string
        word = selection[0]
        return word.lower()  # will return all words in lower case
    except:
        # If file can not be open uses words from a pre-defined list
        print("""Can not find excel file. Please check file exists.
        Word has been taken from backup file.\n""")
        selection = random.choice(words)
        return selection.lower()


def start_game():
    """
    This starts the game once the user has entered a name
    """
    # clears the inital instructions from the screen once the game starts
    display = Display
    display.clear_console()
    word = pick_word()
    word_len = len(word)
    # creates area of underscores that equals length of the word
    answer_area = "-" * len(word)
    answer_list = list(answer_area)
    # empty list to add the guessed letters to once they are inputted
    letters_guessed = []
    lives = 7
    print('Lets start the game\n')
    print(f'Hint: The word is {word_len} letters long\n')
    print(answer_area)

    # if lives is more than 0
    # the loop will keep running
    while lives > 0:
        if ''.join(answer_area) == word:
            print('Woohoo you guessed the word! Winner!!')
            end_game()
            break
        guesses = input('Please guess a letter\n').lower()
        # checks if the guess is only 1 letter and is in the alphabet
        if len(guesses) == 1 and guesses.isalpha():
            if guesses in letters_guessed:
                print(f'You have already guessed {guesses}, try again!')
            elif guesses in word:
                print(f'Woohoo {guesses} is correct.')
                for letters in range(len(word)):
                    if guesses == word[letters]:
                        answer_list[letters] = guesses
                        word[letters] == answer_area[letters]
            else:
                # takes away a life for every wrong guess
                lives = lives - 1
                print(f'{Colors.red}')
                print(hangman_graphic[lives])
                print(f'{Colors.reset}')
                print(f"""Sorry, {guesses} isn't correct.
                You have {lives} lives left. Guess again""")
            # add the guess to a list of letters
            letters_guessed.append(guesses)

        else:
            print('Not a valid letter. Try again :)')
        answer_area = ''.join(answer_list)
        print(f'{Colors.green}')
        print(answer_area)
        print(f'{Colors.reset}')

    if lives == 0:
        print(f'{Colors.red}')
        print(hangman_graphic[lives])
        print(f'{Colors.reset}')
        print(f"""You are out of lives, sorry about that.
        The word was {word}. Better luck next time!""")


def play():
    """
    Asked the user if they would like to play the game and calls
    start_game if they answer yes
    """
    game = input('Please enter Y or N \n').upper()
    if game == 'Y':
        start_game()
    elif game == 'N':
        print('Sorry to see you go so soon!')
    else:
        print('Please enter a valid answer')
        play()


def end_game():
    """
    Askes the user if they would like to play again
    """
    game = input('Are you ready to play again? Y or N\n').upper()
    if game == 'Y':
        Display.clear_console()
        start_game()
    elif game == 'N':
        print('Sorry to see you go. Come back again soon!')
    else:
        print('Please enter a valid answer')
        end_game()


def main():
    """
    The main function that calls all other functions
    """
    welcome_message()
    play()
    end_game()


main()
