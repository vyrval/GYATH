'''
Created on Jan 6, 2016

@author: T0157129
'''
import logging
import logging.config

from Items.PotionObject import PotionObject

class MyCharacter:
    '''
    This class represents a basic character.
    
    Attributes:
        int HP : represents the Health Points of the character.
            If HP==0 the character is dead
            
        dict equipment : represents the equipment of the character.
            weapon    : the character's active weaponObject
            armor     : the character's active armorObject
            
        dict bag : represents the bag of the character. Here will be stored every found item.
            HP_potion   : the number of HP potions that the character owns.
            <item_name> : any found itemObject.
    
    
    Functions:
        boolean isAlive()
    
    '''

    def __init__(self, HP, name, level):
        '''
        Constructor
        '''


        self.HPinit= HP
        self.HP = HP
        self.name = name
        self.level= level
        self.gold= 0
        
        self.equipment= {}
        self.equipment["weapon"]=None
        self.equipment["armor"]=None
        
        self.bag={}
    
    '''
    boolean isAlive()
        Return true if HP > 0
    '''
    def isAlive(self):
        return self.HP>0
    
    
    
    ########################################
    #    EQUIPMENT management
    ########################################
    '''
    void equipWeapon(weaponObject)
        Equip the character with the weaponObject.
        If a weapon is already equipped, the old one is added to the bag.
    '''
    def equipWeapon(self, weaponObject):
        if weaponObject is not None:
            actualWeapon= self.equipment["weapon"]
            if actualWeapon is not None:
                self.addToBag(actualWeapon)
            
            self.equipment["weapon"]= weaponObject
#             self.logger.info("Weapon equipped: %s" % weaponObject.name)
            
    '''
    void equipArmor(armorObject)
        Equip the character with the armorObject.
        If an armor is already equipped, the old one is added to the bag.
    '''
    def equipArmor(self, armorObject):
        if armorObject is not None:
            actualArmor = self.getArmor()
            if actualArmor is not None:
                self.addToBag(actualArmor)
            
            self.equipment["armor"]= armorObject
#             self.logger.info("Armor equipped: %s" % armorObject.name)

    '''
    weaponObject getWeapon()
        Return the equipped weapon.
        Can be None
    '''            
    def getWeapon(self):
        weapon = self.equipment["weapon"]
        self.equipment["weapon"]= None
        return weapon
    
    '''
    armorObject getArmor()
        Return the equipped armor.
        Can be None
    '''            
    def getArmor(self):
        armor = self.equipment["armor"]
        self.equipment["armor"]= None
        return armor
    
    
    
    ########################################
    #    BAG management
    ########################################
    '''
    void listInventory()
        Print the content of the character's bag
    '''
    def listInventory(self):
        print( '-- INVENTORY OF %s CONTAINS:' % self.name)
        for itemName in self.bag.keys():
            print ("    |%s" % self.bag[itemName]) 
    
    '''
    void addToBag(itemObject)
        Add itemObject to the bag.
        The key for this object is the itemObject.name 
    '''
    def addToBag(self, itemObject):
        self.bag[itemObject.name()]= itemObject
        print("Item put in bag: %s" % itemObject.name())
    
    '''
    itemObject getFromBag(itemName)
        Get the object named "itemName" from the bag.
        If there is no itemObject named like this in the bag, return None. 
    '''
    def getFromBag(self, itemName):
        return self.bag[itemName]
    
    '''
    itemObject takeFromBag(itemName)
        Get the object named "itemName" from the bag.
        The object is no longer in the bag.
        If there is no itemObject named like this in the bag, return None. 
    '''
    def takeFromBag(self, itemName):
        return self.bag.pop(itemName)
    
    def removeFromBag(self, itemName):
        self.bag.pop(itemName)
    
    
    '''
    void useFromBag(itemName)
        If an item with this name is found, call its use function.
    '''
    def useFromBag(self, itemName):
        item= self.bag.get(itemName)
        if item is not None:
            if item.get('usable') is None:
                print('Not usable')
                return
            else:
                #If it's not a potion we remove the object from the bag
                if not isinstance(item, PotionObject):
                    item= self.takeFromBag(itemName)
                        
                if item is None:
                    print("No such object in the bag.")
                else:
                    item.use(self)
        else:
            print("none obj") 
                
    
    ########################################
    #    FIGHT management
    ########################################
    '''
    void defend(damagePoints)
        The character loose HP depending on his armor and damagePoints.
    '''
    def defend(self, damagePoints):
        armor= self.equipment["armor"]
        
        if armor != None:
            m_damagePoints = damagePoints - armor.defensePoints()
            if m_damagePoints < 0:
                m_damagePoints=0
        else:
            m_damagePoints = damagePoints
        
        self.HP = self.HP - m_damagePoints
        print("%s has lost %d HP..." % (self.name,m_damagePoints))
        
    
    '''
    void attack(characterObject)
        The character attacks characterObject. 
        If the character has no weapon, do nothing.
    '''
    def attack(self, characterObject):
        weapon = self.equipment["weapon"]
        
        if weapon != None:
            print("%s attacks." % self.name)
            characterObject.defend(weapon.attackPoints())
        else:
            print("%s can't attack, no weapon..." % self.name)
        
        
        
    ########################################
    #    Other functions
    ########################################
        
    '''
    unitsUsed fillHP(units)
        Refill HP bar with units points.
        Return the number of units recovered. 
        (Can be:    0 if HP == HPinit
                 or units
                 or the difference between HP and HPinit if HP+units > HPinit)   
    '''
    def fillHP(self, units):
        unitsUsed= 0
        if self.HP < self.HPinit:
            #Restore HP 
            if self.HP + units >= self.HPinit:
                unitsUsed= self.HPinit - self.HP
            else:
                unitsUsed= units
            self.HP= self.HP + unitsUsed
            print("%s recovered %d HP." % (self.name, unitsUsed))
        else:
            print("%s HP already full." % self.name)
            
        return unitsUsed
        