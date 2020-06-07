

import time

playersinventory = ['']
invincinity = ['']

shopinventory = ['Health Potion',         '$','Gun 44.',               '$80' ]

#shop modules
#a filter to reocunt all coins (since I kept them sperate entaitys)
def coincount():
    coins = 0
    global playersinventory
    for el in playersinventory:
        try:
            coins += (int(el))
            playersinventory.remove(int(el))
        except ValueError:
            pass
    playersinventory.append(coins)
    print('you have',coins,"coins")

def coinbuy(price,item):
    global coins
    coins = 0
    global playersinventory
    for el in playersinventory:
        try:
            coins += (int(el))
            playersinventory.remove(int(el))
        except ValueError:
            pass
    coins -= price
    if coins > 0:
        playersinventory.append(item)
        playersinventory.append(coins)


#a buy fuction
def buy(x):
    if x == 'buyhealthpotion':
        coinbuy(15,'Health Potion')
    else:
        if x == 'buygun':
            coinbuy(80, 'Gun 44.')


#cheaking if item is in inventory
def use(x):
    availtouse = x in playersinventory
    if availtouse == True:
        return True
    else:
        return False
#adding items invinitys to invneotry
def take(x):
    available = x in invincinity
    if available == True:
        playersinventory.append(x)
        print(x,'added to inventory')
    else:
        print("that item isn't around here")


#An introsequesnce
def intro():
    print(
        'You open your eyes, and light floods in you stand in an archway \n Infront of you see a '
        'giant gold gate, \n to your left you see a blue door \n to your right are two doors one Purple and one Magenta \n behind '
        'you connected to the archway is a portal, and behind it you can just make out a Brown door')
    print(
        'to your north west is a building, behind you to the west is man'
        ' with a ship to his back and a board to his side "Trivia 4 Money" is scribed  "')
    print(' A old man appears infront of you from the corner of your eye "hello my child')
    time.sleep(6)
    print('hello, will you speak to me')
    time.sleep(6)
    print('\n \n \n oh boy you must not know how talking works in this world" to speak, enter "say<A, B or C>" eg sayG')
    print('A = Where am I')
    print('B = Who are you')
    print('C = Thank You')
    canswer = input('\n')
    if canswer == 'sayA':
        print(
            'Oh your in GameWorld, within the BlueMoon Arcade, you came in here a '
            'few moments ago following the evil wizard lambada, who kidnapped you friend \n if you memory is hazy it is ok it happends'
            ' often to traveller')
        print('anything else you would like to ask \n')
        print('A = Who are you \nB = No thanks')
        celse = input()
        if celse == 'sayA':
            print("I'm Gerald the Grey, Wizard of GameWorld")
        else:
            print('Well ok then')
    else:
        if canswer == "sayB":
            print("I'm Gerald the Grey, Wizard of GameWorld")
            print(' A = Where am I \nB = Nothing Thanks')
            celse = input('\n')
            if celse == "sayA":
                print(
                    'Oh your in GameWorld, within the BlueMoon Arcade, you came in here a few '
                    'moments ago following the evil wizard lambada, who kidnaped you friend')
            else:
                print('Ok')
        else:
            print("you're very welcome")
            print('A = where am I \nB = Who are you')
            celse = input('\n')
            if celse == 'say A':
                print(
                    'Oh your in GameWorld, within the BlueMoon Arcade, you came in here a few moments ago following the evil wizard lambada, who kidnaped you friend')
                print('anything else you would like to know')
                print('A = Who are you')
                csubelse = input('\n')
                if csubelse == "sayA":
                    print("I'm Gerald the Grey Wizard of GameWorld")

            else:
                print("I'm Gerald the Grey Wizard of GameWorld")
                print('anything else you would like to know')
                print('A = Where am I\n B = No Thanks')
                csubelse = input('\n')
                if csubelse == "sayA":
                    print(
                        'Oh your in GameWorld, within the BlueMoon Arcade, you came in here a few moments ago following the evil wizard lambada, who kidnaped you friend')
                else:
                    print('well ok them')
#single use module parameter doen't matter
def tutorial(x, y):
    print('Well since your new to this world, how about I go though some basic things with you ')
    print('In game world we use basic commands "use", "go", "take" and the one you already know "say" ')
    print("What skill would you like to practise, how about you tell me what you want to start")

    #this bit will runn through until the player partises all the skills
    sprac = ['A = use', 'B = take', 'C = go']
    while len(sprac) != 0:
        print(sprac)
        choice = input('what will it be?')
        if choice == "sayA":
            sprac.remove('A = use')
            print("Ok then Use this command allows you to utilize the items in your inventory\n here i'll give you an item ")
            playersinventory.append(x)
            print(playersinventory, 'is your current inventory')
            print('How now use that item enter "usefartbombscroll"')
            susefbs = input()
            if susefbs == 'usefartbombscroll':
                if use(x) == True:
                    print('Eww Sorry young man that was indeed a bad idea for your first item use')
        else:
            if choice == 'sayB':
                sprac.remove('B = take')
                print("Ok to use the take command, here i'll drop a dragon claw")
                print('enter takedragonclaw to pick up this claw')
                invincinity.append(y)
                stake = input()
                if stake == 'takedragonclaw':
                    take(y)
            else:
                if choice == "sayC":
                    sprac.remove('C = go')
                    print('Ok let me show you how the go command works')
                    print('ok in this game you have to movment options walk and run Walk = A and Run = B')
                    print('now enter goleft')
                    sgowhere = input()
                    if sgowhere == "goleft":
                        print('oh boy where are you going off to enter goright to come back here')
                        scomeback = input()
                        if scomeback == "goright":
                            print('well their  you have it, thats game work')
    print("keep in mind no capitals and spaces in commands\n, you can cheak whats in your inventory by using the showinventory command\n"
          "and you can use the leave command to leave any game"
          "\nSince you came here to save your friend I want to give you a hint, you need 4 keys to get into Lamada's castle he's hidden the keys in keyrooms avaivlable in each room\nthe catch is the rooms themselfs are locked, maybe you can go cheak out how to open them")
coins = 0
