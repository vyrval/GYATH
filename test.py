from Prefabs.WorldItems import WorldItems
from Items.PotionObject import PotionObject
from Characters.Player import Player


import xml.dom.minidom as minidom

WI= WorldItems()
pot = WI.getPotionByCategory('HP')


print(pot.data)

val = pot.get('usable')
print(val is None)

P1= Player()
P1.addToBag(pot)

print(P1)
P1.listInventory()

P1.useFromBag("HP_potion")




# 
# 
# file = minidom.parse("./XML_Files/PotionsFile.xml")
# potions = file.getElementsByTagName("Potion")
# 
# for potion in potions:
#     data={}
#     for attrName, attrValue in potion.attributes.items():
#         #attrName= attrName.replace('u\'', '')
#         attrName= (String)(attrName)
#         print(type(attrName))        
#         data[attrName]=attrValue
#         


print("end")