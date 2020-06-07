
import time
import random
import turtle
from gamefuncts import *


playersinventory = []
invincinity = []

shopinventory = ['Health Potion         $20',
                 'Gun 44.               $80'
                 ]



def gotopoof():
    print('you arrive in a small 3 doored room but the the sign lays borken, and the portals black as night you see a hand reach out from one on the poratls\n'
          'and a voice yelp "help" ')
    while 'poofkeyroomkey' not in playersinventory:

        whattodo = input('do you wish to save this creature say yes or no ')
        if whattodo == 'sayyes':
            print('the creature drops key4 and dies')
            invincinity.append('key4')
            take('key4')


        else:
            if whattodo == "sayno":
                print('hestless man Game=Over')

            else:
                print('pleasep pick an option')


def gotoholmes(beated):
    print('you can leave any of the rooms my simply typing leave')
    while beated != 'y':
        inholmes()
        whattodo = input('What should Sherlock to next')
        if whattodo == 'goguard':
            guard()
        else:
            if whattodo == 'golivingroom':
                holmeslivingroom()
            else:
                if whattodo == 'goupstairs':
                    upstairs()
                else:
                    if whattodo =='goright':
                        turnright()
                    else:
                        if whattodo == 'goleft':
                            turnleft()
                        else:
                            if whattodo == 'gohallway':
                                hallway()
                            else:
                                if whattodo == 'leave':
                                    return
                                listofverbs(whattodo)

def gotowaterfight():
    print(
        ' Welcome to waterfight, ever played a FPS shooter, well we created the one your 4 year old should be playing, assume the role of James an'
        'essectirc 12 year old at the world water-ballon fight championship ')
    print('say start to start')
    start = '0'
    while start != 'saystart':
        start = input()
        if start == 'saystart':
            print(
                'Welcome to the Infinate area, defending champs the 02s face off aging H2Win, team 02 has set its 13 members inside the play arena ')
            print('Ready ')
            time.sleep(1)
            print('Set')
            time.sleep(1)
            print('Go')
            print('your team enters the area and is imediatly shot down, by a hidden 02 member, '
                  'while you are able to cover him before he can get you')
            time.sleep(2)
            print('you must do this alone')
            defeated = 0
            shots = 0
            choices = []
            while defeated < 12:
                print('this portion of the game is unfinished, for your curoicty in coming here here is a gift ')
                coins = 15
                invincinity.append('poofkeyroomkey')
                take('poofkeyroomkey')
                invincinity.append(coins)
                take(coins)
                return







def gotostore(playersinventory, invincinity,shopinventory):
    print("you arrive at the a store\n their is a store keeper with a gleaming smile on his face"
          'would you like to see my stores kind sir')
    answer = input('what would you like to say to the shop keeper')
    if answer == 'sayyes':
        print('the man smiles "wonderful" \n\n',shopinventory)
        print('you can use the buy command to buy anything I have for a price ofcourse *remember no capitals or spaces in Gameworld')
        coincount()
        buy = input('what can I interest you in?')
        buy(buy)
    else:
        if answer == 'sayno':
            print("well comeback soon")
            print('the nice shopkeeper then kicks you out')
        else:
            print('this was a simple question, say yes, or say no')

def gotolegendofszelda(invneotry,invincility,coins ):
    beatmonsters = 'n'
    visited = 0
    beenhere = 0
    cask = 0
    while beatmonsters != 'y':

        if visited == 0:
            losinroom(invincinity, playersinventory)
            visited += 1
        sgo = input()
        if sgo == "golivingroom":
            inlivingroom(invincinity,playersinventory)
        else:
            if sgo == 'gooutside':
                print('you head their')
                outside(invincinity,playersinventory)
            else:
                if sgo == 'goforest':
                    forest(invincinity,playersinventory)
                else:
                    if sgo == 'gomountain':
                        moutain(invincinity,playersinventory,cask)
                    else:
                        if sgo == 'gojump':
                            jump()
                        else:
                            if sgo == 'goseeview':
                                seeview()
                            else:
                                if sgo == "govilla":
                                    outside(invincinity, playersinventory)
                                else:
                                    if sgo == 'gocaves':
                                        caves(beenhere)
                                    else:
                                        if sgo == "goleft":
                                            goleft()
                                        else:
                                            if sgo == 'goright':
                                                goright()
                                            else:
                                                if sgo == 'gocastle':
                                                    gocastle()
                                                else:
                                                    if sgo == 'gothroneroom':
                                                        gothroneroom()
                                                    else:
                                                        if sgo == 'leave':
                                                            print("you've left")
                                                            return
                                                        else:
                                                            listofverbs(sgo)

def gotobossroom(keys, items):
    if 'key1' in playersinventory:
        if 'key2' in playersinventory:
            if 'key3' in playersinventory:
                if 'key4' in playersinventory:
                    print('you are in a boss room, turns out your lambada is a crying child, and his mom just needed your friend to calm him down\n if only you had inner peace ')
                    if input('psst, use innerpeace') == 'useinnerpeace':
                        print('with ture inner peace the childs crying seizes')
                        print('Yay you win this game you winner you')
    else:
        print("you lack 4 keys, you can't get int here")
