'''
Created on Feb 23, 2016

@author: T0157129
'''

'''
dict 
    Fill and return a dictionary filled with the attributes of the Xml_elemt
'''
def parseAttributes(Xml_elemt):
    data={}
    for attrName, attrValue in Xml_elemt.attributes.items():
        data[(str)(attrName)]=(str)(attrValue)
    return data