'''
Created on Jan 7, 2016

@author: T0157129
'''



import random
import xml.dom.minidom as minidom

from Items.ArmorObject import ArmorObject
from Items.WeaponObject import WeaponObject
from Items.PotionObject import PotionObject
from Utilities import XmlParser as xmlp

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
        self.__initPotionsDict()
        
        self.WeaponsDict={}
        self.__initWeaponsDict()
        
        self.ArmorsDict ={}
        self.__initArmorsDict()
        
        self.ItemsDict  ={}
        self.__initItemsDict()
        
        self.dictList=[]
        self.dictList.append(self.PotionsDict)
        self.dictList.append(self.WeaponsDict)
        self.dictList.append(self.ArmorsDict)
        self.dictList.append(self.ItemsDict)
        
        
    def __initPotionsDict(self):
        self.PotionsDict["HP"]={}
        self.PotionsDict["MP"]={}
        
        self.__FillPotionsDictFromXML("./XML_Files/PotionsFile.xml")
        
        
    def __initWeaponsDict(self):
        self.WeaponsDict["notPlayerUsable"]={}
        self.WeaponsDict["basic"]={}
        self.WeaponsDict["common"]={}
        self.WeaponsDict["epic"]={}
        self.WeaponsDict["legendary"]={}
        
        self.__FillWeaponsDictFromXML("./XML_Files/WeaponsFile.xml")
        
        
    def __initArmorsDict(self):
        self.ArmorsDict["notPlayerUsable"]={}
        self.ArmorsDict["basic"]={}
        self.ArmorsDict["common"]={}
        self.ArmorsDict["epic"]={}
        self.ArmorsDict["legendary"]={}
        
        self.__FillArmorsDictFromXML("./XML_Files/ArmorsFile.xml")
        
        
    def __initItemsDict(self):
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
    def __FillArmorsDictFromXML(self, fileName):
        '''
        
        '''
        
        file = minidom.parse(fileName)
        armors = file.getElementsByTagName("Armor")
        for armor in armors:
            data= xmlp.parseAttributes(armor)            
            self.ArmorsDict[data.get('category')][data.get('name')]= ArmorObject(data)
       
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
    def __FillWeaponsDictFromXML(self, fileName):
        file = minidom.parse(fileName)
        weapons = file.getElementsByTagName("Weapon")
        for weapon in weapons:
            data= xmlp.parseAttributes(weapon)             
            self.WeaponsDict[data.get('category')][data.get('name')]= WeaponObject(data)
            
       
    def __FillPotionsDictFromXML(self, fileName):
        file = minidom.parse(fileName)
        potions = file.getElementsByTagName("Potion")
        
        for potion in potions:
            data= xmlp.parseAttributes(potion) 
            self.PotionsDict[data.get('category')][data.get('name')]= PotionObject(data)
          
            
            
    ########################################
    #    get random Item from the dictionaries
    ########################################  
    '''
    armorObject getArmorByCategory(category)
        Return a random armor in the given category
    '''
    def getArmorByCategory(self, category):
        return self.__getItemFromDictByCategory(self.ArmorsDict, category)
    '''
    WeaponObject getWeaponByCategory(category)
        Return a random weapon in the given category
    '''
    def getWeaponByCategory(self, category):
        return self.__getItemFromDictByCategory(self.WeaponsDict, category)
    '''
    Potion getPotionByCategory(category)
        Return a random potion in the given category
    '''
    def getPotionByCategory(self, category):
        return self.__getItemFromDictByCategory(self.PotionsDict, category)
    '''
    Item getItemByCategory(category)
        Return a random item in the given category
    '''
    def getItemByCategory(self, category):
        return self.__getItemFromDictByCategory(self.ItemsDict, category)
    
    '''
    Item getItemFromDictByCategory(mdict, category)
        Return a random item in the given mdict, within the given category.
    '''
    def __getItemFromDictByCategory(self, mdict, category):
        ItemsInCat= mdict[category]
        ItemName= random.choice(list(ItemsInCat.keys()))
        item= ItemsInCat[ItemName].getCopy()
        return item
    
    
    
    
    def getWeapon(self, weaponName):
        return self.__getItemFromDict(self.WeaponsDict, weaponName)
    def getArmor(self, armorName):
        return self.__getItemFromDict(self.ArmorsDict, armorName)
    def getPotion(self, potionName):
        return self.__getItemFromDict(self.PotionsDict, potionName)
    
    def __getItemFromDict(self, mdict, ItemName):
        for category in mdict.keys():
            if mdict[category].has_key(ItemName):
                return mdict[category][ItemName].getCopy()
        return None
    
    
    
    def get(self, ObjectName):
        for mdict in self.dictList:
            object= self.__getItemFromDict(mdict, ObjectName)
            if object is not None:
                return object
        print("[DEBUG]---%s----- %s not found in lib." % (self.__class__.__name__, ObjectName))
        return None
