from Prefabs.WorldItems import WorldItems


import xml.dom.minidom as minidom

WI= WorldItems()
weapon= WI.getWeaponByCategory('basic')
print(weapon.attackPoints())
print(type(weapon.attackPoints()))


print("end")