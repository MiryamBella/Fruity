import requests
from pyquery import PyQuery as pq

import DAL.web_data.DataFromWeb as webData

class cosharot:
    def __init__(self, nameFile):
        self.fruits=webData.getDataFromJyson(nameFile)
        if(self.fruits==None):
            self.fruits = self.makeData(nameFile)

    def get_f(self):
        return self.fruits

    def __str__(self):
        return f"{self.fruits}"

    def getString_orderFruits(self):
        finalStr=""
        for fruit in self.fruits:
            finalStr+= "name: "+ fruit["name"]
            finalStr+='\n'
            finalStr += "text: " + fruit["text"]
            finalStr+='\n'
            finalStr += "link: " + fruit["link"]
            finalStr+='\n'
        return finalStr

    def makeData(self, nameFile):
        # get html from website.
        response = requests.get('https://www.kosharot.co.il/index2.php?id=7&lang=HEB')
        html = pq(response.text)
        # get the data of the fruits.
        divs = html.find("div")
        div = webData.getClassObject(divs, "page3_table_contant")

        fruits = webData.getDataAsList(div, "https://www.kosharot.co.il/")

        for i in range(len(fruits)):
            webData.enrichData(fruits[i], "essayText")

        webData.saveDataAsJson(nameFile, fruits)
        return webData.getDataFromJyson(nameFile)

    def getFruite(self, nameFruit, listFruites):
        for fruit in listFruites:
            if(nameFruit in fruit['name']):
                return fruit['text']

    def getString_orderFruit_byIndex(self, index):
        finalStr=""
        finalStr+= "name: "+ self.fruits[index]["name"]
        finalStr+='\n'
        finalStr += "text: " + self.fruits[index]["text"]
        finalStr+='\n'
        finalStr += "link: " + self.fruits[index]["link"]
        finalStr+='\n'
        return finalStr

    def getString_orderFruit_byName(self, name):
        finalStr=""
        index=0
        i=0
        for f in self.fruits:
            if(name in f["name"]):
                index=i
            i+=1
        finalStr+= "name: "+ self.fruits[index]["name"]
        finalStr+='\n'
        finalStr += "text: " + self.fruits[index]["text"]
        finalStr+='\n'
        finalStr += "link: " + self.fruits[index]["link"]
        finalStr+='\n'
        return finalStr

'''
cosharotData= cosharot("jsonFiles/fruitsList.json")

#print(cosharotData)
#print(cosharotData.getString_orderFruit_byIndex(0))
#print(cosharotData.get_f()[0])
print(cosharotData.getFruite("תמר", cosharotData.get_f()))
'''



# my try:
#print(cosharotData.getString_orderFruits())

#print(cosharotData.getString_orderFruit_byName("תפוח"))
