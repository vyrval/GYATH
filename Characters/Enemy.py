'''
Created on Jan 7, 2016

@author: T0157129
'''

from Characters.Character import MyCharacter

class Enemy(MyCharacter):
    '''
    classdocs
    '''


    def __init__(self, category, name, description, HP, lvl):
        '''
        Constructor
        '''
        MyCharacter.__init__(self, HP, name, lvl)
        self.description = description
        self.category = category
        
    def __str__(self):
        string= """
                    %s
                    %s
                    HP: %s
                    Level: %s
                    Weapons: %s
                    Armor: %s
                    -------------""" \
                % (self.name, self.description, self.HP, self.lvl, self.equipment["weapon"], self.equipment["armor"])
        
        return string