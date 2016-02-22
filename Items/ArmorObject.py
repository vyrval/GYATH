'''
Created on Jan 6, 2016

@author: T0157129
'''

from Items.Item import Item


class ArmorObject(Item):
    '''
    classdocs
    '''


    def __init__(self, category, name, description, cost, defensePoints):
        '''
        Constructor
        '''
        Item.__init__(self, category, name, description, cost)
        self.defensePoints= defensePoints
        
    def __str__(self):
        string= "%s, %s, Defense: %s" % (self.name, self.description, str(self.defensePoints))
        return string