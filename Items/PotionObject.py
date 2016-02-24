'''
Created on Jan 13, 2016

@author: T0157129
'''

from Items.Item import Item

from Utilities import UserInteract as ui



class PotionObject(Item):
    '''
    category can be "MP" or "HP"
    '''


    def __init__(self, data):
        '''
        Constructor
        '''      
        Item.__init__(self, data)
        self.set("contentMax", 100)
        self.set("content", 0 )
        
    def getCopy(self):
        Pot= PotionObject(self.data)
        return Pot
    
    
    def isFull(self):
        return self.get("content") == self.get("contentMax")
    def isEmpty(self):
        return self.get("content") == 0
    
    
    '''
    void fill()
        Fill the potion to contentMax.
    '''
    def fill(self):
        if self.isFull():
            print("%s already full." % self.name())
        else:
            self.set("content", self.get("contentMax"))
            print("%s is now full." % self.name())
    
    '''
    int use(character)
        Use "units" units of the bottle.
        Return the units used 
            may be different of entry if:
                        unitsToUse > content
                        AND/OR
                        (character.HPInit - c.HP ) < unitsToUse
    '''
    def use(self, character):
        if self.isEmpty():
            print("%s is empty..." % self.name())
        else:
            units= self.__getUnits()
            if self.category() == "HP":
                unitsToUse= units
                if self.get('content') < unitsToUse:
                    unitsToUse = self.get('content')
                    
                unitsUsed= character.fillHP(unitsToUse)
                self.set("content", self.get('content') - unitsUsed)
                print("%d/%d units remaining in %s." % (self.get('content'), self.get('contentMax'), self.name()))
            
    '''
    units __getUnits()
        Asks the user how many units does he wants to use.
        Return the number of units.
    '''
    def __getUnits(self):
        units=ui.userInputInt("How many do you want to use? (%d units remaining) " % (self.get('content')))
        return units
        
    
    def __str__(self):
        string= "%s, %s. Contains %d/%d unit of potion." % (self.name(), self.description(), self.get('content'), self.get('contentMax'))
        return string