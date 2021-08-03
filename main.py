# Python RPG-DiceRoller
# ver 0.1
# By LohanGuedes

import random

def main():
    # Welcome user
    print("Python RPG-DiceRoller")
    print("Welcome Player!")
    print("For help on the usag type h or H")
    # User Variables:
    splited_inp = []

    # Game state Variables
    gameover = False
    stillplay = None
    num_plays = 0
    # mainloop
    while(True):
        print("Enter the dices you want to roll!")
        splited_inp = input().split()

        if splited_inp == 'h' or splited_inp == 'H':
            print('HELP!')
            pass
        if splited_inp:
            print("You runned: ")
            for user_Inp in splited_inp:
                print(user_Inp + ':', rolldice(user_Inp))
            num_plays += 1
            stillplay = input("Do you want to roll again? [Y/n] ")
            pass


        # Game State
        if stillplay == 'n' or stillplay == 'N':
            gameover = True
        if stillplay == 'y' or stillplay == 'Y':
            gameover = False
            pass
        # Quit Game
        if gameover == True:
            break

def rolldice(dice):
    rolled_dices = []
    try:
        if '+' in dice:
            splited = dice.split('+')
            mod = +int(splited[-1])
            just_dice = splited[0]
            just_splited = just_dice.split('d')
        elif '-' in dice:
            splited = dice.split('-')
            mod = -int(splited[-1])
            just_dice = splited[0]
            just_splited = just_dice.split('d')
        else:
            mod = 0
            just_splited = dice.split('d')
            pass 

        num_dices = int(just_splited[0])
        num_faces = int(just_splited[1])
       
        i = 0
        while i < int(num_dices):
            rolled_dices.append(random.randint(1, num_faces) + mod)
            i += 1       
        return rolled_dices
    except:
        return "Sorry, This input was not expected. Jumping to the next one. For help type: h"

# def wish_to_log(stdvar):
#     wsh = input("Do you want to store or print the log [n/Y]")
#     if wsh == 'y' or wsh == 'Y':
#         print('1. Store the log into a file')
#         print('2. Print the Log here.')
#         option = input('Chose your option:  ') 
#         if option == 2:
#             print(stdvar)
#     else:
#         pass
    

if __name__ == "__main__":
    main()
    # wish_to_log(result_string)
    pass
