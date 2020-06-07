


import random
import turtle
import time
from Funct import *
from gamesfunct import *
from tkinter import messagebox


#messagebox.showinfo("Title", "a Tk MessageBox")
#Poof Modueles


#Holmes Modules
def inholmesmainframe():

    print('you arrive in a small room whit three doors.\n'
            'this is a sign with an explanation\n\n\n'
            'this is the Holmes mainframe\n There are three doors the leftmost door is a *keyroom, enter-able once the mystey is solved\n'
            'the middle door is *holmes a game where you can assume the persona of the famous detective Sherlock Holmes,\n'
            'the right is a *suspectroom, where you can pick the murderer,who'
            'quick reminder sherlock can use the investigate command to well investigate anything you can investigate ')

def inholmes():
    print('you dismount from the carriage, and infront of a home, their is a man at the door a *guard perhaps he has some more information as to why the Chief called you here')


def guard():
    print('you approch the guard you says"Ok so your Sherlock, honour to meet you, boss wants you to look at a body\nwith a well meaning but rough shove'
          'you in a hallway  "')
def carriage():
    print('the carriage races away before you can even muster a sound, guess you have no choice but to go to the *guard ')

def hallway():
    print('an officer apporcahes, well their you are  Mr.Sherlock the bodys upstairs just turn left,\n'
          'theres a dauther to her rooms on the right, theres a living room our detectives have alreay looked at it maybe you can find somthing   '
          '')
    print('you can go to the *livingroom or *upstairs')
def holmeslivingroom():
    print('in the living room')

def upstairs():
    print('do you want to turn left or right')

def turnleft():
    print('you head into the body room lady lies dead in the middle of the room')
    whattodo = input('want to invesigate, room or body')
    if whattodo == 'room':
        print('nothing special about the room')
    else:
        if whattodo == 'body':
            print('find a tiffany blue nail chip in the victims hair')
            if 'nailpolish' in playersinventory:
                print('the murder just unrraveled  itself, you know who the killer is')
            else:
                print('you could find the orign of this chip you would know the killer')


def turnright():
    print('you head into the daughter room')
    cinvestiage = input('type investigate to see Sherlocks conclutions')
    if cinvestiage == 'investigate':
        print('nothing, special for a teenage girl,their is some spilled tiffany blue nail polish on the bed with the daughets name engraved on the bottle\n, you should take it for evidence')
        takeit = input('take the *nailpolish')
        if takeit == 'takenailpolish':
            invincinity.append('nailpolish')
            take('nailpolish')

def suspectroom():
    print('an officer apporches, you these are the'"'"'uns we rounded up ser the husband, the daugther, the butler and the maid ')
    whotopick = input('say who you think is the susptect A = Husband B = Daugther C = Butler and D = Maid')
    if whotopick == 'sayB':
        print('the daughter screems out, how did you know, she is dragged out by 2 constables. \n a officer approcher you i think this is youres')
        invincinity.append('holmeskeyroomkey')
        take('holmeskeyroomkey')
        global holmesbeat
        holmesbeat = "y"
    else:
        if whotopick == 'leave':
            return
        else:
            print('you just forsok an inocent person to death, Game Over, Restart the program')





#Trivia game
def triviagame():
    coins = 100
    invincinity.append(coins)
    print('hey, wow, this is bug bug, beepboop, heres 100 coins')
    take(coins)


#Waterfight fuctions
def number():
   global shots
   shots += 1
def timer():
    global time
    global shots
    time += .1  # Increase the global time variable.
    print(round(time, 1))
    if time < 3:
       # Call `timer` function again after 100 ms.
       turtle.ontimer(timer, t=100)
       number()
       global shots
       if shots == 1:


        print("time's up close the dialogue box")
def tangogenerator():
    if random.randint(1, 2) == 1:
        print('an team 02 member suddeny appears press spacebar as many times as posibble ')
        global shots
        global time
        shots = 0
        time = -0.1  # -0.1 because the `timer` adds .1 immediately.
        timer()
        turtle.onkey(number, 'space')
        print(shots)
        needed = random.randint(15,35)
        turtle.mainloop()
        if shots > needed:
            global defeated
            defeated += 1
            print("you got him")
            print (defeated)


#Legend of szelda tings

def losstarttext(vistedlos):
    if vistedlos == 0:
        print('you arrive in a small room with two doors\n '
              'their is a sign in the middle with an explaiation\n\n\n'
              '"this is the mainframe room one door is the legend of Szelda game\n'
              'and the other is a keyroom, though it has been locked\n\n\n'
              'the right door has a long complicated label, you will porbably need to get *closer to read it'
              '\nthe other says "*los"\n ')
        vistedlos += 1
    else:
        print("you've read the sign")

def losinroom(alist, inventory):
    coins = 12
    global invincinity
    invincinity.append(coins)
    global playersinventory
    print('you are in a room, around you their is only one door that leads to your *livingroom , on a shelf are some coins ')
    print('what do you want to do')
    whattodo = input()
    if whattodo == 'takecoins':
        take(coins)
    else:
        print('whoops, please enter that instruction again')

def inlivingroom(invincinity, inventory):
    print('you are in a living room, their is a door that leads *outside')


def outside(invincinity, inventory):
    print('you stand outside a house, the gate says Ethernet *villa, their is a path that leads forward, along it as sign says "to *forest"')

def forest(invicinty,iventory):
    print('you arrive in the forest, old wooden signs denote where 4 paths lead, to one side it read *mountain\n One reads *caves\n one reads *castle and one reads Ethernets *villa')

def moutain(invincinity, inventory,casked):
    if casked == 0:
        print('on your way there you overhear an old man taking to him self "The caves, rope, the dead ahh ')
        casked += 1
    print(', The gray claw shaped peaks rise high above your head, their seems to be a plateau at the top, if only you could climb it the *forest lies a path away')
    if 'logic' in inventory:
        print('perhaps some kind of rope')
    whattodo = input()
    if whattodo == 'userope' :
        if use('rope'):
            goup()
        else:
            print("you don't seem to have any rope, perhaps if you find some")


def goup():
    print('you use that hard earned rope to pull yourself to the top of the mountaion\n'
          'their are obvioulsy only two options go *jump or go *seeview ')

def jump():
    coins = 1
    print("wow, how stupid can you even be, just this one time for your patheticness, heres a coin, just don't do this again")
    invincinity.append(coins)
    take(coins)
    print('you wake wake up agin, but this time in the middle of the forest, you see three signs around you *caves\n, *mountain(you know what'
    'you now allowed in here anymore\n and *castle')
    return


def seeview():
    print('its a truly beautifull view')
    playersinventory.append('Inner Peace')
    print('inner peace has been added to your inventory, not like its any use though ')

def caves(cbeenhere):
    print('you head over to the caves')
    if cbeenhere == 0:
        cbeenhere += 1
        print("it looks pretty dark and cold in their who knows what could be lurking")
        whertogo = input('what should you do, go in?')
        if whertogo == 'goin':
            print('inside the caves you can just make out two dimly lit doors you can go *left, from behind this door you can here suffocated groans'
                  '\nthe *right one has a thin parcel of light coming in from the crevaces')
            term = 12
    if term != 12:
        print('inside the caves you can just make out two dimly lit doors you can go *left, from behind this door you can here suffocated groans'
                      '\nthe *right one has a thin parcel of light coming in from the crevaces')

def goleft():
    if 'sword' not in playersinventory:
        print('you approch the door as you closer to the door and the sound grow louder and lounder, perhaps its not safe to enter here without a weapon')
    else:
        if 'sword' in playersinventory:
            print('you swing open the door only to find 5 undead creatures, at the far end you see some rope, ')
            if 'logic' in playersinventory:
                print('that could be very usefull, perhaps for climbing a mountain')
            print('press a then enter as fast as posible or else.... ')
            fight( 'zombie',5)
def goright():
    print('as you apdproch the room you can hear som sort of rythmic chanting from inside\n insdie you see a grizzled old man ')
    global invincinity
    invincinity.append('sword')
    print("It's dangerous to go alone take this sword")
    whattodo = input('take it child, enter takesword')
    if whattodo == 'takesword':
        take('sword')
        print('the old man then users you out of the caves')
def gocastle():
    print('you arrive at the castle\n you imeriadly get attcked by werewolves\n *usesword or go back to *forest quick')
    start = time.time()
    gmail = input()
    end = time.time()
    if end - start < 10:
        if gmail == 'usesword':
            fight('werewolves',18,15)
            print('you can head into the *throneroom now')
        else:
            if gmail == 'goforest':
                pass
    else:
        if end - start > 8:
            print('wow, you did it only like a death to late, argg stuipid players, why are you walking into a castle withouts sword\n \nGame Over\nrestart 25c ')

def gothroneroom():
    print('you arrive in the throneroom')
    fight("Wi-fi", 10, 3)
    print('wow a key sits on the throne room, you could probably use it to open that keyroom from earlier\na name tagged, tagged on with fancy string says\n'
          'legendofszeldakeyroomkey')
    invincinity.append('legendofszeldakeyroomekey')
    whattodo = input()
    if whattodo == 'takelegendofszeldakeyroomkey':
        take('legendofszeldakeyroomkey')



#a Fight
def fight(monster, secs, numberofthings):
    zombieskilled = 1
    while zombieskilled < numberofthings:
        print('a',monster, 'approaches')
        time.sleep(random.randint(1,4))
        start = time.time()
        attack1 = 'temp'
        while attack1 != 'a':
            attack1 = input('now!')
        end = time.time()
        if end - start < secs:
            print('you got that one but their are more coming')
            zombieskilled += 1
            secs -= 1
    if monster == 'zombie':
        print('all',monster,'s beat, well done, grab that rope')
        global invincinity
        invincinity.append('rope')
        doyouwant = input()
        if doyouwant == 'takerope':
            take('rope')
        else:
            print('oops byte overload re-enter that please')

#hiddent easter egg of sorts, but also my pass off fuction that tells the user if their action is not doable
def listofverbs(x):
    averblist = ['jump','squat', 'hop', 'fly ', 'die','think']
    if x in averblist:
        print(' why, you must be enjoying yourself, not like you have a friend to save from a evil wizard to anything')
    else:
        print(" Welp you don't want to break the game while your in it, that isnt a thing you can do")

def legendofszeldakeyroom():
    if 'legendofszeldakeyroomkey' in playersinventory:
        global invincinity
        coins = 15
        invincinity = [coins, 'key1']

        print('you stick the key into the keyhole'
            '\ninside their are two tables one with a key, one of the keys to lambadas castle on the other are some coins ')
        print('\n',*10," hi I'm the deveoper of this game and i'm a lazy person what can I say, so lets make a deal just type 'takeeboth'\n and i'll put both into you ivnetoyr capish GameDev out"
                       "\n"*10)
        whattodo = 'n'
        while whattodo != 'takeeboth':
            whattodo = input('what do you wantodo')
            if whattodo == 'takeeboth':
                take("key1")
                take(coins)
            else:
                print('really, really, I as game dev come to you in game and tell you to type takeeboth and this, not listening to me is how you repay me\n '
                      'tsk,tsk, tsk I should just Gameover here but I am in a good mood')
    else:
        print("you can't come in here yet, abra-cadabra backtohub")
        return

def waterfightkeyroom():
    if 'waterfightkeyroomkey' in playersinventory:
        global invincinity
        coins = 15
        invincinity = [coins, 'key3']

        print('you stick the key into the keyhole'
              '\ninside their are two tables one with a key, one of the keys to lambadas castle on the other are some coins ')
        print('\n', *10,
              " hi I'm the deveoper of this game and i'm a lazy person what can I say, so lets make a deal just type 'takeeboth'\n and i'll put both into you ivnetoyr capish GameDev out"
              "\n" * 10)
        whattodo = 'n'
        while whattodo != 'takeeboth':
            whattodo = input('what do you wantodo')
            if whattodo == 'takeeboth':
                take("key3")
                take(coins)
            else:
                print('really, really, I as game dev come to you in game and tell you to type'
                      ' takeeboth and this, not listening to me is how you repay me\n '
                      'tsk,tsk, tsk I should just Gameover here but I am in a good mood')
    else:
        print("you can't come in here yet, abra-cadabra backtohub")
        return

def poofkeyroom():
    if 'poofkeyroomkey' in playersinventory:
        global invincinity
        coins = 15
        invincinity = [coins, 'key4']

        print('you stick the key into the keyhole'
              '\ninside their are two tables one with a key, one of the keys to lambadas castle on the other are some coins ')
        print('\n', *10,
              " hi I'm the deveoper of this game and i'm a lazy person what can I say, so lets make a deal just type 'takeeboth'\n and i'll put both into you ivnetoyr capish GameDev out"
              "\n" * 10)
        whattodo = 'n'
        while whattodo != 'takeeboth':
            whattodo = input('what do you wantodo')
            if whattodo == 'takeeboth':
                take("key4")
                take(coins)
            else:
                print('really, really, I as game dev come to you in game and tell you to type'
                      ' takeeboth and this, not listening to me is how you repay me\n '
                      'tsk,tsk, tsk I should just Gameover here but I am in a good mood')
    else:
        print("you can't come in here yet, abra-cadabra backtohub")
        return

def holmeskeyrrom():
    if 'holmeskeyroomkey' in playersinventory:
        global invincinity
        coins = 15
        invincinity = [coins, 'key2']

        print('you stick the key into the keyhole'
            '\ninside their are two tables one with a key, one of the keys to lambadas castle on the other are some coins ')
        print('\n',*10," hi I'm the deveoper of this game and i'm a lazy person what can I say, so lets make a deal just type 'takeeboth'\n and i'll put both into you ivnetoyr capish GameDev out"
                       "\n"*10)
        whattodo = 'n'
        while whattodo != 'takeeboth':
            whattodo = input('what do you wantodo')
            if whattodo == 'takeeboth':
                take("key2")
                take(coins)
            else:
                print('really, really, I as game dev come to you in game and tell you to type'
                      ' takeeboth and this, not listening to me is how you repay me\n '
                      'tsk,tsk, tsk I should just Gameover here but I am in a good mood')
    else:
        print("you can't come in here yet, abra-cadabra backtohub")
        return

