'''
Created on Jan 7, 2016

@author: T0157129
'''
import libxml2
import random

from Items.ArmorObject import ArmorObject
from Items.WeaponObject import WeaponObject


class WorldItems:
    '''
    This class contains every Item of the game world.
    Items are splited into different dictionaries containing dictionaries:
        PotionsDict 
            for HP and MP potions.
            keys:
                HP_potion
                MP_potion
        WeaponsDict
            for weapons
            keys:
                basic
                common
                epic
                legendary
        ArmorsDict
            for armors
            keys:            
                basic
                common
                epic
                legendary        
        ItemsDict
            for...
            keys:
                key :)
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
        self.PotionsDict={}
        self.initPotionsDict()
        
        self.WeaponsDict={}
        self.initWeaponsDict()
        
        self.ArmorsDict ={}
        self.initArmorsDict()
        
        self.ItemsDict  ={}
        self.initItemsDict()
        
       
        
        
    def initPotionsDict(self):
        self.PotionsDict["HP_potion"]={}
        self.PotionsDict["MP_potion"]={}
        
    def initWeaponsDict(self):
        self.WeaponsDict["notPlayerUsable"]={}
        self.WeaponsDict["basic"]={}
        self.WeaponsDict["common"]={}
        self.WeaponsDict["epic"]={}
        self.WeaponsDict["legendary"]={}
        
        self.FillWeaponsDictFromXML("./WeaponsFile.xml")
        
    def initArmorsDict(self):
        self.ArmorsDict["notPlayerUsable"]={}
        self.ArmorsDict["basic"]={}
        self.ArmorsDict["common"]={}
        self.ArmorsDict["epic"]={}
        self.ArmorsDict["legendary"]={}
        
        self.FillArmorsDictFromXML("./ArmorsFile.xml")
        
        
    def initItemsDict(self):
        self.ItemsDict["key"]={}
    
    
    ########################################
    #    Fill the dictionaries
    ########################################
    '''
    void FillArmorsDictFromXML(fileName)
        Open the XML file named "fileName" and look for Armors.
        The XML should look like this:
            <Armors>
                <Armor 
                    category="basic"
                    name="clothes"
                    description="Simple clothes. Not a great defense."
                    defensePoints="1"
                    cost="10"/>
                ...
            </Armors>
    '''
    def FillArmorsDictFromXML(self, fileName):
        file = libxml2.parseFile(fileName)
        root = file.children
        armor = root.children
        while armor is not None:
            if armor.type == "element":
                category        = armor.prop("category")
                name            = armor.prop("name")
                desc            = armor.prop("description")
                defensePoints   = int(armor.prop("defensePoints"))
                cost            = int(armor.prop("cost"))
                
                self.ArmorsDict[category][name]= ArmorObject(category, name, desc, cost, defensePoints)
            armor= armor.next
        
    '''
    void FillWeaponsDictFromXML(fileName)
        Open the XML file named "fileName" and look for Weapons.
        The XML should look like this:
            <Weapons>
                <Weapon 
                    category="basic"
                    name="wooden sword"
                    description="Well... Actually it's just a stick..."
                    attackPoints="1"
                    cost="1"/>
                ...
            </Weapons>
    '''
    def FillWeaponsDictFromXML(self, fileName):
        file = libxml2.parseFile(fileName)
        root = file.children
        weapon = root.children
        while weapon is not None:
            if weapon.type == "element":
                category        = weapon.prop("category")
                name            = weapon.prop("name")
                desc            = weapon.prop("description")
                attackPoints    = int(weapon.prop("attackPoints"))
                cost            = int(weapon.prop("cost"))
                
                self.WeaponsDict[category][name]= WeaponObject(category, name, desc, cost, attackPoints)
            weapon= weapon.next     
        
    ########################################
    #    get random Item from the dictionaries
    ########################################  
    '''
    armorObject getArmorByCategory(category)
        Return a random armor in the given category
    '''
    def getArmorByCategory(self, category):
        return self.getItemFromDictByCategory(self.ArmorsDict, category)
    '''
    WeaponObject getWeaponByCategory(category)
        Return a random weapon in the given category
    '''
    def getWeaponByCategory(self, category):
        return self.getItemFromDictByCategory(self.WeaponsDict, category)
    '''
    Potion getPotionByCategory(category)
        Return a random potion in the given category
    '''
    def getPotionByCategory(self, category):
        return self.getItemFromDictByCategory(self.PotionsDict, category)
    '''
    Item getItemByCategory(category)
        Return a random item in the given category
    '''
    def getItemByCategory(self, category):
        return self.getItemFromDictByCategory(self.ItemsDict, category)
    
    '''
    Item getItemFromDictByCategory(mdict, category)
        Return a random item in the given mdict, within the given category.
    '''
    def getItemFromDictByCategory(self, mdict, category):
        ItemsInCat= mdict[category]
        ItemName= random.choice(list(ItemsInCat.keys()))
        return ItemsInCat[ItemName]
    
    
    
    
    def getWeapon(self, weaponName):
        return self.getItemFromDict(self.WeaponsDict, weaponName)
    def getArmor(self, armorName):
        return self.getItemFromDict(self.ArmorsDict, armorName)
    
    def getItemFromDict(self, mdict, ItemName):
        for category in mdict.keys():
            if mdict[category].has_key(ItemName):
                return mdict[category][ItemName]
        return None