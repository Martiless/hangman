import os


class Colors:
    """
    To add colors to the main game file
    """
    reset = '\033[0m'
    black = '\033[30m'
    red = '\u001b[31;1m'
    green = '\u001b[32;1m'
    blue = '\u001b[36;1m'


class Display:
    """
    Holds all the visual aspects of the game
    """

    def clear_console():
        """
        Checks to see what os if the computer is running Windows
        This piece of code was taken from www.delfstack.com
        """
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)
