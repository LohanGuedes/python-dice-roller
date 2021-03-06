# Python RPG-DiceRoller
# By LohanGuedes

import random

def main():
    # Welcome user
    log_and_print("Python RPG-DiceRoller")
    log_and_print("Welcome Player!")
    
    # User Variables:
    splited_inp = []

    # Game state Variables
    gameover = False
    stillplay = None
    num_plays = 0

    # mainloop
    while(True):
        log_and_print("Enter the dices you want to roll!")
        split_inp = input().split()

        if split_inp == 'h' or split_inp == 'H':
            log_and_print('HELP!')
        if split_inp:
            print("You rolled: ")
            for user_Inp in split_inp:
                log_and_print(f"{user_Inp}: {rolldice(user_Inp)}")
            num_plays += 1
            stillplay = log_and_input("Do you want to roll again? [Y/n] ")


        # Game State
        if stillplay.upper() == 'N':
            gameover = True
        if stillplay.upper() == 'Y':
            gameover = False
        # Quit Game
        if gameover == True:
            break
            
## Log Functions
def log(text: str, logfile: str="mylog.txt"):
    with open(logfile, "a") as f:
        f.write(text)

def log_and_print(text: str):
    print(text)
    log(f"{text} \n")

def log_and_input(prompt: str):
    i = input(prompt)
    log(f"{prompt}: {i} \n")
    return i

# Game dice roller
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

        num_dices = int(just_splited[0])
        num_faces = int(just_splited[1])
       
        i = 0
        while i < int(num_dices):
            rolled_dices.append(random.randint(1, num_faces) + mod)
            i += 1       
        return rolled_dices
    except:
        return "Sorry, This input was not expected. Jumping to the next one"

if __name__ == "__main__":
    main()
    log_and_print("====================================================================================")
