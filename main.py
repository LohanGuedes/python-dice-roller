# Python RPG-DiceRoller
# ver 0.1
# By LohanGuedes

import random

def main():
    # Welcome user
    print("Python RPG-DiceRoller")
    print("Welcome Player!")
    #User Variables:
    splited_inp = []


    gameover = False
    stillplay = None
    # mainloop
    while(True):
        num_plays = 0
        print("Enter the dices you want to roll!")
        splited_inp = input().split()
        print(splited_inp)
        for dice in splited_inp:
            rolldice(dice)


        stillplay = input("Do you want to roll the dice again? [Y/n] ")
        if stillplay == 'n' or stillplay == 'N':
            gameover = True
            pass
        
        if gameover == True:
            break
        
            
        
def rolldice(dice):
    rolled_dices = []
    if '+' in dice:
        splited = dice.split('+')
        mod = splited[-1]
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
        rolled_dices.append(random.randint(1, num_faces))
        i += 1       
    print(rolled_dices)
    return rolled_dices

if __name__ == "__main__":
    main()
    pass
