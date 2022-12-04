import requests
from pyquery import PyQuery as pq
import json
import codecs



#from bidi import algorithm as bidialg

#to get the table of ftuits as div object.
def getDataDiv(divs, classContectText):
    for index in range(len(divs)):
        div = divs.eq(index)
        if div.has_class(classContectText):
            return div

def getData(divBase):
    friutList = divBase.find("a")
    list = []
    for index in range(len(friutList)):
        fruitBox = friutList.eq(index)
        fruit = getDataFromA(fruitBox)
        fruit['index'] = index
        list.append(fruit)
    return list

#convert tha data from a to dicshenery.
def getDataFromA(a):
    name = a.text()
    link = a.attr('href')
    result = {"name": name, "link": "https://www.kosharot.co.il/" + link}
    return result


def enrichData(fruit):
    #go to the link of website.
    response = requests.get(fruit['link'])
    html = pq(response.text)
    divs = html.find("div")
    div = getDataDiv(divs, "page7_table_data")
    text = div.find("p").text()
    fruit['text'] = text


def saveDataAsJson(nameFile, data):
    stream = codecs.open(nameFile, 'w', encoding = "utf-8-sig")
    # Serializing json
    json_object = json.dumps(data, indent=4)
    stream.write(json_object)
    #json.dump(json_object, stream)
    stream.close()

def saveDataAstext(nameFile, data):
    stream = codecs.open(nameFile, 'w', encoding = "utf-8-sig")
    for objy in data:
        stream.write(str(objy))
    #json.dump(json_object, stream)
    stream.close()

def getText():
    i = 0
    for fruit in fruits:
        enrichData(fruit)
        i = i + 1
        if (i % 10 == 0):
            print(i)
        if (i > 100):
            return

def getDataFromJyson(nameFile):
    stream = codecs.open(nameFile, 'r', encoding="utf-8-sig")
    # Serializing json
    json_object = json.load(stream)
    print(json_object)
    # json.dump(json_object, stream)
    stream.close()






