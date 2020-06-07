

from Funct import *
from gamesfunct import *

#
#Filename         : MohJawBlueMoon
#Program Outline  : Brief description: A game where your main character is trapped in a arcade and must "beat"
# the evil wizard Lambada to save himself and his friend.
#Programmer       : <Jawad>
#Class            : ICS203-02
#DueDate          : Dec. 15 - 2017
#


#this is an intro
intro()

tutorial('fartbombscroll', 'dragonclaw')

print('The Old sage, disappears just as he has appeard, you look around once again, with your know found knowledge you know your goal now, '
      "to your Front in Lamada's Castle, inside your friend, you can see the four keyholes now, "
      "all around you are the four games of the bluemoon arcade *legendogszelda, *holmes, *poof or *waterfight " )

#if the game has been won or not
cgamewon = 'n'
#this will shtop when the game has been won
while cgamewon != 'y':
    whereto = input('where do wanna go ')
    #the waterfight level
    if whereto == 'gowaterfight':
        print('you walk through the portal on other side lies a small room with two doors'
              'both conviniantly are labeled one says keyroom and the other says game seeing that the keyroom is locked you head into the game\nyou can probably come back later')
        gotowaterfight()
    else:
        #the legend of Szelda level
        if whereto == 'golegendofszelda':
            losstarttext()
            losgo = input('would you like to go *closer or to *los')
            if losgo == 'gocloser':
               legendofszeldakeyroom()
            else:
                if losgo == 'golos':
                    gotolegendofszelda(playersinventory, invincinity, coins)
        else:
            #the poof levels
            if whereto == 'gopoof':
                gotopoof()
            else:
                #The holmes level
                if whereto == "goholmes":
                    holmesbeat = 'n'
                    inholmesmainframe()
                    while holmesbeat != 'y':
                        whattodo =  input('what room do you want to go in')
                        if whattodo == 'goholmes':
                            gotoholmes(holmesbeat)
                        else:
                            if whattodo == 'gokeyroom':
                                holmeskeyrrom()
                            else:
                                if whattodo == 'gosuspectroom':
                                    suspectroom()
                                else:
                                    if whattodo == 'leave':
                                        pass
                                    else:
                                        listofverbs(whattodo)

                else:
                    #store
                    if whereto == "gostore":
                        gotostore(playersinventory,invincinity,shopinventory)
                    else:
                        #Triva minigame goto
                        if whereto == "gotrivia":
                            triviagame()
                        else:
                            #just areminder
                            if whereto == "gohub":
                                print('You are in thehub')
                            else:
                                #the final passover
                                if whereto == "showinventory":
                                    print(playersinventory)

