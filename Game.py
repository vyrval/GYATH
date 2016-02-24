'''
Created on Jan 6, 2016

@author: T0157129
'''
import logging
import logging.config


from Characters.Player import Player
from Prefabs.WorldItems import WorldItems
from Prefabs.EnemyGenerator import EnemyGenerator
from Printer import Printer
from Stories.Story import Story

from Utilities import XmlParser as xmlp
from Utilities import UserInteract as ui
from Utilities import Caster as cast


import xml.dom.minidom as minidom


class Game:
    '''
    This class represents the whole game.
     
    '''


    def __init__(self):
        '''
        Constructor
        '''
#         logging.basicConfig(level=logging.DEBUG, disable_existing_loggers=False)
#         self.logger = logging.getLogger(__name__)
        
        self.gameOver= False
        
        
        self.printer=Printer(self)
        
        self.WI= WorldItems()
        
        self.player = self.__initPlayer()
        
        
        # Enemies
        self.EG = EnemyGenerator(self.WI)
        
        self.currentEnemy= ""
        
        
        self.story = Story( self)
    
        self.printer.intro(self.player)
        self.player.listInventory()
        raw_input()
        
        self.nbTurn = 0
        
        print("##################################################")
        print("                THE GAME BEGINS")
        print("##################################################")
        
        self.nextEvent = self.story.goToEvent("intro")
        
        
    '''
    void onTurn()
    '''    
    def onTurn(self):
        self.nbTurn = self.nbTurn +1
        
        self.nextEvent = self.story.goToEvent(self.nextEvent)
                
        
        
    '''
    boolean onGame()
        Return true while the player isn't dead.
    '''       
    def onGame(self):
        return self.player.isAlive() and self.nbTurn<20
    
    
    def endGame(self):
        print("##################################################")
        print("                 THE GAME ENDS")
        print("##################################################")
        self.gameOver= True
        
    def isGameOver(self):
        return self.gameOver
    
    
    '''
        Return a player object.
    '''
    def __initPlayer(self):
        
        dictMode={} #will contains all information about each game mode
        file = minidom.parse("./XML_Files/InitPlayer.xml")
        modes = file.getElementsByTagName("DifficultyMode")
        for mode in modes:
            data= xmlp.parseAttributes(mode)             
            dictMode[data.get('id')]= data
        
        #Ask the player which mode does he wants to play
        ToPrint="Difficulty Modes: "
        for mode in dictMode.keys():
            ToPrint= ToPrint + ' ' + mode
        
        print(ToPrint)
        
        #Parse the user input
        userMode = ui.userIput("Which mode do you want to play? ", dictMode.keys())
        SelectedMode = dictMode[userMode]
        
        ## Parse the mode's parameters
        player = Player(SelectedMode.get('hp'))
        
        armorName =SelectedMode.get('armor') 
        if armorName is None:
            player.equipArmor(self.WI.getArmorByCategory("basic"))
        else:
            player.equipArmor(self.WI.getArmor(armorName))
            
        weaponName = SelectedMode.get('weapon')
        if weaponName is None:
            player.equipWeapon(self.WI.getWeaponByCategory("basic"))
        else:
            player.equipWeapon(self.WI.getWeapon(weaponName))
            
        potion = self.WI.getPotionByCategory("HP")
        if SelectedMode.get('potion') is not None:
            if cast.strToBool(SelectedMode.get('potion')):  
                potion.fill()
        player.addToBag(potion)
        
        return player