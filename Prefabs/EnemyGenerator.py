'''
Created on Jan 7, 2016

@author: T0157129
'''

import random
import xml.dom.minidom as minidom
import logging
import logging.config

from Characters.Enemy import Enemy


class EnemyGenerator:
    '''
    This object give the possibility to instantiate an enemy.
    '''


    def __init__(self, WorldItems):
        '''
        Constructor
        '''
#         logging.basicConfig(level=logging.DEBUG, disable_existing_loggers=False)
#         self.logger= logging.getLogger(__name__)
                
        self.enemiesDict={}
        self.WI = WorldItems
        
        self.__initEnemiesDict()
    
    
    def __initEnemiesDict(self):
        self.enemiesDict["basic"]={}
        self.enemiesDict["common"]={}
        self.enemiesDict["epic"]={}
        self.enemiesDict["legendary"]={}
        self.__FillEnemiesDictFromXML("./XML_Files/EnemiesFile.xml")
        
#         self.logger.debug("ENEMIES -----------------")
#         self.logger.debug(self.enemiesDict)
        
        
    '''
    void FillEnemiesDictFromXML(fileName)
        Open the XML file named "fileName" and look for Enemies.
        The XML should look like this:
            <Enemies>
                <Enemy 
                    category="basic"
                    name="rat"
                    description="A common rat that uses claws or fangs."
                    HP="20"
                    level="1"
                    weapon="claws"
                    armor="leather"/>
                ...
            </Enemies>
    '''
    def __FillEnemiesDictFromXML(self, fileName):
        file = minidom.parse(fileName)
        enemys = file.getElementsByTagName("Enemy")
        for enemy in enemys:
            category    = enemy.attributes["category"].value
            name        = enemy.attributes["name"].value
            desc        = enemy.attributes["description"].value
            HP          = int(enemy.attributes["HP"].value)
            level       = int(enemy.attributes["level"].value)
            weaponName  = None
            armorName   = None
            if "weapon" in enemy.attributes.keys():
                weaponName  = enemy.attributes["weapon"].value
            if "armor" in enemy.attributes.keys():
                armorName   = enemy.attributes["armor"].value
            expPoints   = int(enemy.attributes["xp"].value)
            
            myEnemy= Enemy(category, name, desc, HP, level, expPoints)
            self.prepareEnemy(myEnemy, armorName, weaponName)
         
            
    '''
    Enemy getEnemyByCategory(category)
        Return an enemy in the given category.
    '''    
    def getEnemyByCategory(self, category):
        EnemiesInCat= self.enemiesDict[category]
        EnemyName= random.choice(list(EnemiesInCat.keys()))
        return EnemiesInCat[EnemyName].getCopy() 
    
    
    '''
    Enemy getEnemyByName(name)
        Return the enemy "name" if it exists. None otherwise.
    '''
    def getEnemyByName(self, name):
        for category in self.enemiesDict.keys():
            enemy = self.enemiesDict[category].get(name)
            if enemy is not None:
                return enemy.getCopy()
        return None
    
    '''
    void prepareEnemy(self, EnemyObj, armorName, weaponName)
        Add weapon and armor to EnemyObj
        and add it to the enemiesDict.
    '''
    def prepareEnemy(self, EnemyObj, armorName, weaponName):
        if armorName is not None and armorName !="":
            armor = self.WI.getArmor(armorName)
            EnemyObj.equipArmor(armor)
        if weaponName is not None and weaponName !="":
            weapon = self.WI.getWeapon(weaponName)
            EnemyObj.equipWeapon(weapon)
        
        self.enemiesDict[EnemyObj.category][EnemyObj.name]= EnemyObj