from colorama import Fore, Back, Style


#class Colors:
   # RED = "\u001b[31m",
   # GREEN = "\u001b[32m",
   # BLUE = "\u001b[34m",
   # YELLOW =  "\u001b[33m",
   # PURPLE =  "\u001b[35m"


#print(f'{Colors.BLUE} This is blue text.')


print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')
