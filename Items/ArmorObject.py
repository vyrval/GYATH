'''
Created on Jan 6, 2016

@author: T0157129
'''

from Items.Item import Item


class ArmorObject(Item):
    '''
    classdocs
    '''


    def __init__(self, data):
        '''
        Constructor
        '''
        Item.__init__(self, data)
        self.data["defensePoints"]= (int)(data.get("defensePoints"))
        
        
    def use(self, character):
        character.equipArmor(self)
        
    def defensePoints(self):
        return self.get('defensePoints')
        
            
    def __str__(self):
        string= "%s, %s, Defense: %s" % (self.name(), self.description(), str(self.defensePoints()))
        return string
    
    def getCopy(self):
        return ArmorObject(self.data)