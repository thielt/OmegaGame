from sys import exit 

life = 3
#included for memory allocation for win or lose scenario

def start():
    global life #reusing stored memory
    name = input("Enter Name: ")
    name = name.capitalize() #name is altered on output ex. george becomes George
    
def path():
    global life #keeps life amount in memory despite how many restart attempts there are
    p_chosen = input("Left or Right?: ")
    p_chosen = p_chosen.casefold() #aggresive method for lower case strings, reinitializing variable of chosen path taken

    if p_chosen == "left": 
        print("Went left.")
        death()
    elif p_chosen == "right":
        print("Went right.")
        fight()
    else:
        print("Invalid choice.")
        path() #always recursively call for all other test cases
h_sythr = h_player = 100
def fight():
    global life
    
    def display():  #redisplayed every move
        global life
        print(f"Sythr: {h_sythr}")
        print(f"Player: {h_player}")

    while h_player > 0 and h_sythr > 0:
        move = input("Dodge or Attack?: ")
        move = move.casefold()

        if move == "dodge":
            h_player -= 20
            display()
        elif move == "attack":
            h_sythr -= 50
            display()
        else: 
            print("Invaid input.")
            global h_player
            global h_sythr
            fight()

    if h_player == 0:
        death()
    else:
        win()

def win():
    global life
    print("Win. You received an extra life.")
    life += 1
    print(f"You have {life} lives.")
    print("Sythr defeated but will respawn again...")
    if_respawn()

def if_respawn():
    replay = input("Play again?(y/n): ")
    replay = replay.casefold()
    if replay == "y":
        #start() name input no longer neccessary 
        print("AS EXPECTED, HE'S BACK!!!!")
        path()
    elif replay == "n":
        exit()
        #could use 'pass' to call empty if statement
    else:
        print("Invalid input.")
        if_respawn()

def death():
    restart = input("You died, try again?(y/n): ")
    restart = restart.casefold()
    global life

    if life == 1:
        print("LAST CHANCE. TRY YOUR BEST.")
    if restart == "y":
        if life > 0:
            life -= 1
            print(f"{life} live(s) left.")
            print("Restarting...")
            print("A new day has come...")
            path()
        else:
            print("No more lives.")
            exit()
    elif restart == "n":
        pass
    else:
        print("Not valid. (y/n)?")
        death()

if __name__ == '__main__': #main call for first compile and run 
    start()
    path()
