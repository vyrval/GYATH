'''
Created on Jan 14, 2016

@author: T0157129
'''


from Utilities.Switch import switch

import logging

class Action:
    '''
    classdocs
    '''


    def __init__(self, XmlAction, gameObj):
        self.logger= logging.getLogger(__name__)
        '''
        Constructor
        '''
        
        self.game= gameObj

        #Parse properties
        
        self.name       = XmlAction.attributes["action"].value
        if self.name == "fight":
            self.enemy = XmlAction.attributes["enemy"].value
        
        self.nextEvent  = XmlAction.attributes["value"].value
        
    
    def doIt(self):
        
        for case in switch(self.name):
            if case('fight'):
                enemy= self.game.EG.getEnemyByName(self.enemy)
                player = self.game.player
                
                while player.isAlive() and enemy.isAlive() :
                    print("# # # # # # # # # # # # # # # #")
                    self.game.printer.character(player)
                    self.game.printer.character(enemy)
                    print("- - - - - - - - - - - - - - - -")
                    
                    player.fight(enemy)
                    if enemy.isAlive():
                        enemy.attack(player)
                    else: 
                        print("You've defeated the %s!!!" % enemy.name)
                        player.gainExp(enemy.expPoints)
                    print("# # # # # # # # # # # # # # # #")
                    raw_input()
                    
                enemy= None
                
                if player.isAlive():
                    return self.nextEvent
                else:
                    self.game.endGame()
                    return "die"
                break
            
            if case('die'):
                return None
                break
            
            if case(): # default, could also just omit condition or 'if True'
                return self.nextEvent
                # No need to break here, it'll stop anyway
    
    def __str__(self):
        return self.name