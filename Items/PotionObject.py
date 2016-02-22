'''
Created on Jan 13, 2016

@author: T0157129
'''

from Items.Item import Item

class PotionObject(Item):
    '''
    category can be "MP" or "HP"
    '''


    def __init__(self, data):
        '''
        Constructor
        '''
        data["contentMax"]  = 100
        data["content"]     = 0       
        Item.__init__(self, data)

        
    def getCopy(self):
        data= {}
        data["category"]    =self.category()
        data["name"]        =self.name()
        data["description"] =self.description()
        data["cost"]        =self.cost()
        
        Pot= PotionObject(data)
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
            if self.category == "HP":
                    unitsToUse= units
                    if self.content < unitsToUse:
                        unitsToUse = self.content
                        
                    unitsUsed= character.fillHP(unitsToUse)
                    self.set("content", self.data.get('content') - unitsUsed)
                    print("%d units remaining in %s. (over %d)" % (self.get('content'), self.name(), self.get('contentMax')))
            
    '''
    units __getUnits()
        Asks the user how many units does he wants to use.
        Return the number of units.
    '''
    def __getUnits(self):
        units=0
        valid= False
        
        while not valid:
            units= raw_input("How many do you want to use? ")
            try :
                units_val= int(units)
                valid= True
            except ValueError:
                print("It doesn't make sens...")
        return units_val
        
    
    def __str__(self):
        string= "%s, %s. Contains %d/%d unit of potion." % (self.name(), self.description(), self.get('content'), self.get('contentMax'))
        return string