'''
Created on Jan 7, 2016

@author: T0157129
'''
import libxml2
import random
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
        logging.basicConfig(level=logging.DEBUG, disable_existing_loggers=False)
        self.logger = logging.getLogger(__name__)
        
        
        self.enemiesDict={}
        self.WI = WorldItems
        
        self.initEnemiesDict()
    
    
    def initEnemiesDict(self):
        self.enemiesDict["basic"]={}
        self.enemiesDict["common"]={}
        self.enemiesDict["epic"]={}
        self.enemiesDict["legendary"]={}
        self.FillEnemiesDictFromXML("./EnemiesFile.xml")
        
        self.logger.debug("ENEMIES -----------------")
        self.logger.debug(self.enemiesDict)
        
        
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
    def FillEnemiesDictFromXML(self, fileName):
        file = libxml2.parseFile(fileName)
        root = file.children
        enemy = root.children
        while enemy is not None:
            if enemy.type == "element":
                category    = enemy.prop("category")
                name        = enemy.prop("name")
                desc        = enemy.prop("description")
                HP          = int(enemy.prop("HP"))
                level       = int(enemy.prop("level"))
                weaponName  = enemy.prop("weapon")
                armorName   = enemy.prop("armor")
                
                
                self.logger.debug("Enemy parse from XML")
                self.logger.debug("category: %s" % category)
                self.logger.debug("name: %s" % name)
                self.logger.debug("desc: %s" % desc)
                self.logger.debug("HP: %s" % HP)
                self.logger.debug("level: %s" % level)
                self.logger.debug("weaponName: %s" % weaponName)
                self.logger.debug("armorName: %s" % armorName)
                
                myEnemy= Enemy(category, name, desc, HP, level)
                
                if armorName is not None and armorName !="":
                    armor = self.WI.getArmor(armorName)
                    myEnemy.equipArmor(armor)
                if weaponName is not None and weaponName !="":
                    weapon = self.WI.getWeapon(weaponName)
                    myEnemy.equipWeapon(weapon)
                
                
                self.enemiesDict[category][name]= myEnemy
            enemy= enemy.next
            
    '''
    Enemy getEnemyByCategory(category)
        Return an enemy in the given category.
    '''    
    def getEnemyByCategory(self, category):
        EnemiesInCat= self.enemiesDict[category]
        EnemyName= random.choice(list(EnemiesInCat.keys()))
        return EnemiesInCat[EnemyName] 