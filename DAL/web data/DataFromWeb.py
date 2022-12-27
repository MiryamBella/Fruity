import os.path

import requests
from pyquery import PyQuery as pq
import json
import codecs
#from bidi import algorithm as bidialg




#to get the object block with some class.
def getClassObject(father, classContectText):
    for index in range(len(father)):
        kid = father.eq(index)
        if kid.has_class(classContectText):
            return kid

#to get the object block with some class.
def getManyClassesObject(father, classContectText):
    kids=[]
    for index in range(len(father)):
        kid = father.eq(index)
        if kid.has_class(classContectText):
            kids.append(kid)
    return kids


def getDataAsList(group, linkWeb):
    itemList = group.find("a")
    list = []
    for index in range(len(itemList)):
        itemBox = itemList.eq(index)
        item = getDataFrom_A_box(itemBox, linkWeb)
        item['index'] = index
        list.append(item)
    return list

#convert tha data from a to dicshenery.
def getDataFrom_A_box(a, linkWeb):
    name = a.text()
    link = a.attr('href')
    result = {"name": name, "link": linkWeb + link}
    return result


def enrichData(itemLink, className):
    #go to the link of website.
    response = requests.get(itemLink['link'])
    html = pq(response.text)
    divs = html.find("div")
    div = getClassObject(divs, className)
    text = div.find("p").text()
    itemLink['text'] = text


def saveDataAsJson(nameFile, data):
    stream = codecs.open(nameFile, 'w', encoding = "utf-8-sig")
    # Serializing json
    json_object = json.dumps(data, indent=4)
    stream.write(json_object)
    #json.dump(json_object, stream)
    stream.close()

def saveDataAstext(nameFile, data):
    stream = codecs.open(nameFile, 'w+', encoding = "utf-8-sig")
    for objy in data:
        stream.write(str(objy))
    #json.dump(json_object, stream)
    stream.close()

def getTextFromItemLink(linksList):
    i = 0
    for fruit in linksList:
        enrichData(fruit)
        i = i + 1
        if (i % 10 == 0):
            print(i)
        if (i > 100):
            return

def getDataFromJyson(nameFile):
    if(os.path.exists(nameFile)==False):
        return None
    stream = codecs.open(nameFile, 'r+', encoding="utf-8-sig")
    # Serializing json
    json_object = json.load(stream)
    stream.close()
    return json_object






