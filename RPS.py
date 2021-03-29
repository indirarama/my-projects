import random
import re 
import os
os.system('cls' if os.name=='nt' else 'clear')
while(1<2):
    print("\n")
    print("Rock, Paper, Scissors - Shoot!")
    uchoice=input("Choose Your Input:[R]ock,[P]aper, or [S]cissors:")
    if not re.match("[SsRrPp]",uchoice):
        print("Please choose the first Letter:")
        print("[R]ock, [P]aper, or [S]cissors:")
        continue
    print("Your choice is:" + uchoice)
    choices = ['R' , 'P', 'S']
    opchoice = random.choice(choices)
    print("My choice is:" + opchoice)
    if opchoice == str.upper(uchoice):
        print("Match Draw!!!!")
    elif opchoice == 'R' and uchoice.upper() == 'S':
        print("Rock beats Scissors I Win!!!")
        continue
    elif opchoice == 'S' and uchoice.upper() == 'P':
        print("Scissors beats Paper I Win!!!")
        continue
    elif opchoice == 'P' and uchoice.upper() == 'R':
        print("Paper beats Rock I Win!!!")
        continue
    else:
        print("U Win!!!")
        
        
    